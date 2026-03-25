# créer une playlist sur spotify, rechercher les morceaux de la playlist youtube et ajouter les morceaux à la playlist spotify
import spotipy
import re


class Spotify:
    def __init__(self, access_token: str, spotify_user_id: str):
        self.client = spotipy.Spotify(auth=access_token)
        self.spotify_user_id = spotify_user_id

    def create_spotify_playlist(self, playlist_name, channel_name="YouTube"):
        name = f"{playlist_name} from @{channel_name}"
        playlist = self.client.user_playlist_create(self.spotify_user_id, name)
        self.playlist_id = playlist["id"]
        return self.playlist_id
    
    def norm(self, s: str) -> str: # normalisation des mots pour la recherche
        s = s.lower() # en minuscule
        s = re.sub(r"[^\w\s]", " ", s) # enlève ponctuation
        s = re.sub(r"\s+", " ", s).strip() # enlève espaces
        return s # retourne le texte normalisé

    # Nettoyage du texte pour la recherche de morceaux sur Spotify
    def clean_query(self, text: str) -> str:
        text = re.sub(r"\[[^\]]*\]", "", text) # [Official Video]
        text = re.sub(r"\([^)]*\)", "", text) # (Official Audio)
        text = re.sub(r'".*?"', "", text) # "..."
        text = re.sub(r"\b(official|audio|video|hd|4k|lyric|lyrics|visualizer|vevo|live|remastered)\b", "", text, flags=re.I)
        text = re.sub(r"\s+", " ", text).strip()
        return text

    def search_track(self, title: str, artist: str = ""):
        def norm_words(s: str):
            s = self.norm(self.clean_query(s or ""))
            return [w for w in s.split() if len(w) >= 3]

        # mots normalisés
        title_w = norm_words(title)
        artist_w = norm_words(artist)

        if not title_w:
            return None

        # Requêtes progressives
        t = " ".join(title_w)
        a = " ".join(artist_w)

        queries = [t]
        if a:
            queries.append(f"{t} {a}")
            queries.append(f"{a} {t}")

        # Détection de mentions de versions spéciales (live, remix...) pour ajuster le score et éviter les faux positifs
        raw_title = (title or "").lower()
        version_words = {"live", "remix", "cover", "karaoke", "sped", "slowed", "edit", "mix", "instrumental"}
        query_mentions_version = any(w in raw_title for w in version_words)

        # seuil de score pour accepter une correspondance (à ajuster selon les résultats, plus élevé = plus strict)
        base_threshold = 3
        if len(title_w) >= 4:
            base_threshold = 5
        elif len(title_w) == 3:
            base_threshold = 4

        # mot le plus long (hors stop words) pour bonus de score si présent dans le titre Spotify
        stop = {"official", "audio", "video", "lyrics", "lyric", "visualizer", "vevo", "remastered"}
        candidates = [w for w in title_w if w not in stop]
        longest = max(candidates, key=len, default="")

        for q in queries:
            results = self.client.search(q=q, type="track", limit=10)
            items = results.get("tracks", {}).get("items", [])
            if not items:
                continue

            q_words = set(self.norm(q).split())
            best = None
            best_score = -1

            for tr in items:
                tn = self.norm(tr["name"])
                an_sp = self.norm(" ".join(a["name"] for a in tr["artists"]))
                title_set = set(tn.split())
                artist_set = set(an_sp.split())
                score = len(q_words & title_set) * 2 + len(q_words & artist_set)

                # Pénalité si la version Spotify mentionne une version spéciale (live, remix...) mais pas la requête YouTube, pour éviter les faux positifs sur les covers, lives, remixes...
                spotify_mentions_version = any(w in tr["name"].lower() for w in version_words)
                if spotify_mentions_version and not query_mentions_version:
                    score -= 1 # plus élevé = plus pénalisant

                # Bonus si le mot le plus long est présent dans le titre Spotify
                if longest and longest in title_set:
                    score += 1

                if score > best_score:
                    best_score = score
                    best = tr

            if best and best_score >= base_threshold:
                return best

        return None
    

    def add_tracks_to_playlist(self, track_inputs):
        added_items = [] # [{title, artist, spotify_id}]
        failed_items = [] # [{title, artist, query}]
        track_ids = []

        for item in track_inputs:
            if isinstance(item, dict):
                title = item.get("title", "").strip()
                artist = item.get("artist", "").strip()
                raw_query = f"{title} {artist}".strip()
            else:
                raw_query = str(item).strip()
                title = ""
                artist = ""

            # cleaned = self.clean_query(raw_query)
            track = self.search_track(title=title, artist=artist)

            if track:
                spotify_id = track["id"]
                track_ids.append(spotify_id)

            # si title/artist pas fournis (cas string), on prend ceux de Spotify (si trouvés)
                if not title:
                    title = track.get("name", "")
                if not artist:
                    artist = ", ".join(a["name"] for a in track.get("artists", []))

                added_items.append({
                    "title": title,
                    "artist": artist,
                    "spotify_id": spotify_id,
                })
            else:
                failed_items.append({
                    "title": title,
                    "artist": artist,
                    "query": raw_query,
                })

        if track_ids:
            for i in range(0, len(track_ids), 100):
                batch = track_ids[i:i + 100]
                self.client.playlist_add_items(self.playlist_id, batch)
                print(f"🎵 Ajout de {len(batch)} morceaux (batch {i//100 + 1})")

        if failed_items:
            print(f"❌ Non trouvés ({len(failed_items)}):", [f["query"] for f in failed_items])

        print(f"✅ Total ajouté: {len(track_ids)} morceaux")

        return added_items, failed_items


    # Récupère tous les morceaux d'une playlist Spotify avec pagination
    def get_all_tracks_from_playlist(self, playlist_id, limit=50):
        all_tracks = []
        offset = 0

        while True:
            results = self.client.playlist_items(
                playlist_id,
                limit=limit,
                offset=offset
        )

            items = results.get("items", [])
            if not items:
                break

            all_tracks.extend(items)
            offset += limit

        print(f"🎧 Total récupéré : {len(all_tracks)} morceaux")
        return all_tracks
    
    # Extrait les informations de titre et artiste pour chaque morceau d'une playlist Spotify
    def extract_track_info(self, playlist_items):
        track_queries = []

        for item in playlist_items:
            track = item.get("track", {})
            name = track.get("name")
            artists = ", ".join(a["name"] for a in track.get("artists", []))
            query = f"{name} {artists}"
            track_queries.append(query)

        return track_queries




   
# if __name__ == "__main__":
#     spotify_user_id = SPOTIFY_USER_ID # remplacer plus tard 

#     sp = Spotify(SPOTIFY_USER_ID)
#     playlist_id = sp.create_spotify_playlist("Ma Playlist Test", "Chaîne YouTube")

#     tracks = ["Daft Punk One More Time", "Sade Pearls"] # simulé depuis YouTube
#     added = sp.add_tracks_to_playlist(tracks)

#     print(f"✅ Playlist créée ({playlist_id}) avec {len(added)} morceaux ajoutés")