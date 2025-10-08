from backend.models import youtube_model as yt
from backend.models import spotify_model as sp
from backend.models.spotify_model import SPOTIFY_USER_ID

class Synchronizer:
    def __init__(self, youtube_url, spotify_user_id):
        self.youtube_url = youtube_url
        self.spotify_user_id = spotify_user_id
        self.playlist_id = None
        self.track_ids = []

    def extract_youtube(self):
        self.playlist_id = yt.extract_playlist_id(self.youtube_url)
        self.videos = yt.get_videos(self.playlist_id)
        self.titles = yt.get_titles(self.videos)
        self.artists = yt.get_artists(self.videos)
        self.playlist_name, self.channel_name = yt.get_playlist_info(self.playlist_id)
        return self.titles, self.artists

    def create_spotify_playlist(self):
        self.spotify = sp.Spotify(self.spotify_user_id)
        self.playlist_id = self.spotify.create_spotify_playlist(self.playlist_name, self.channel_name)
        return self.playlist_id

    def add_tracks_to_spotify(self):
        queries = [f"{title} {artist}" for title, artist in zip(self.titles, self.artists)]
        self.track_ids = self.spotify.add_tracks_to_playlist(queries)
        return self.track_ids


if __name__ == "__main__":
    youtube_url = input("🔗 Entrez l'URL de la playlist YouTube : ")
    sync = Synchronizer(youtube_url, SPOTIFY_USER_ID)
    sync.extract_youtube()
    sync.create_spotify_playlist()
    sync.add_tracks_to_spotify()

    print(f"✅ Playlist '{sync.playlist_name}' créée avec {len(sync.track_ids)} morceaux ajoutés")
