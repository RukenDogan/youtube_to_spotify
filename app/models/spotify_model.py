# créer une playlist sur spotify, rechercher les morceaux de la playlist youtube et ajouter les morceaux à la playlist spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env.local")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
SPOTIFY_USER_ID= os.getenv("SPOTIFY_USER_ID")

SCOPE = "playlist-modify-public"

class Spotify:
    def __init__(self, spotify_user_id):
        self.spotify_user_id = spotify_user_id
        self.client = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=SPOTIFY_REDIRECT_URI,
            scope=SCOPE
        ))
        current_user = self.client.me()
        self.spotify_user_id = current_user["id"]

    def create_spotify_playlist(self, playlist_name, channel_name="YouTube"):
        name = f"{playlist_name} from @{channel_name}"
        playlist = self.client.user_playlist_create(self.spotify_user_id, name)
        self.playlist_id = playlist["id"]
        return self.playlist_id


    def search_track(self, query):
        results = self.client.search(q=query, type="track", limit=5)
        tracks = results.get("tracks", {}).get("items", [])
        if not tracks:
            return None
        
        # Découpage de la requête pour séparer titre et artiste
        parts = query.split()
        query_lower = query.lower()

        for track in tracks:
            track_title = track["name"].lower()
            track_artists = " ".join([a["name"].lower() for a in track["artists"]])

            # Vérifie si le titre ET l'artiste sont dans la requête
            if any(word in query_lower for word in track_title.split()) and any(a in query_lower for a in track_artists.split()):
                return track["id"]

        return None

    def add_tracks_to_playlist(self, track_queries):
        track_ids = []
        not_found = []
        for query in track_queries:
            track_id = self.search_track(query)
            if track_id:
                track_ids.append(track_id)
            else:
                not_found.append(query)

        if track_ids:
            self.client.playlist_add_items(self.playlist_id, track_ids)
        return track_ids


   
# if __name__ == "__main__":
#     spotify_user_id = SPOTIFY_USER_ID # remplacer plus tard 

#     sp = Spotify(SPOTIFY_USER_ID)
#     playlist_id = sp.create_spotify_playlist("Ma Playlist Test", "Chaîne YouTube")

#     tracks = ["Daft Punk One More Time", "Sade Pearls"] # simulé depuis YouTube
#     added = sp.add_tracks_to_playlist(tracks)

#     print(f"✅ Playlist créée ({playlist_id}) avec {len(added)} morceaux ajoutés")