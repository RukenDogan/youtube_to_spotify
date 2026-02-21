# créer une playlist sur spotify, rechercher les morceaux de la playlist youtube et ajouter les morceaux à la playlist spotify
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import re


SCOPE = "playlist-modify-public playlist-modify-private"

class Spotify:
    def __init__(self, spotify_user_id):
        self.spotify_user_id = spotify_user_id
        self.client = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            scope=SCOPE
        ))
        self.spotify_user_id = self.client.me()["id"]


    def create_spotify_playlist(self, playlist_name, channel_name="YouTube"):
        name = f"{playlist_name} from @{channel_name}"
        playlist = self.client.user_playlist_create(self.spotify_user_id, name)
        self.playlist_id = playlist["id"]
        return self.playlist_id
    
    # Nettoyage du texte pour la recherche de morceaux sur Spotify
    def clean_query(self, text: str) -> str:
        text = re.sub(r"\[[^\]]*\]", "", text)         # [Official Video]
        text = re.sub(r"\([^)]*\)", "", text)          # (Official Audio)
        text = re.sub(r'".*?"', "", text)              # "..."
        text = re.sub(r"\b(official|audio|video|hd|4k|lyric|lyrics|visualizer|vevo|live|remastered)\b", "", text, flags=re.I)
        text = re.sub(r"\s+", " ", text).strip()
        return text


    def search_track(self, query):
        results = self.client.search(q=query, type="track", limit=5)
        tracks = results.get("tracks", {}).get("items", [])
        if not tracks:
            return None
        
        # Découpage de la requête pour séparer titre et artiste
        query_lower = query.lower()

        for track in tracks:
            track_title = track["name"].lower()
            track_artists = " ".join([a["name"].lower() for a in track["artists"]])

            title_terms = track_title.split()
            artist_terms = track_artists.split()

            if all(term in query_lower for term in title_terms + artist_terms):
                return track
            
        return None
    

    def add_tracks_to_playlist(self, track_inputs):
        added_items = []   # [{title, artist, spotify_id}]
        failed_items = []  # [{title, artist, query}]
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

            cleaned = self.clean_query(raw_query)
            track = self.search_track(cleaned)

            if track:
                spotify_id = track["id"]
                track_ids.append(spotify_id)

            # si title/artist pas fournis (cas string), on prend ceux de Spotify
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