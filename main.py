from app.models import youtube_model as yt
from app.models import spotify_model as sp

class Synchronizer:
    def __init__(self, youtube_url, spotify_user_id):
        self.youtube_url = youtube_url
        self.spotify_user_id = spotify_user_id
        self.playlist_id = None
        self.track_ids = []

    def __repr__(self):
        return f"Main(youtube={self.youtube}, spotify={self.spotify})"
    
    def extract_youtube(self, playlist_url):
        self.playlist_url = playlist_url
        self.playlist_id = yt.extract_playlist_id(playlist_url)
        self.videos = yt.get_videos(self.playlist_id)
        self.titles = yt.get_titles(self.videos)
        self.artists = yt.get_artists(self.videos)
        
        self.playlist_name, self.channel_name = yt.get_playlist_info(self.playlist_id)
        return self.titles, self.artists


    def create_spotify_playlist(self):
        name = f"{self.playlist_name} from @{self.channel_name}"
        self.playlist_id = sp.create_playlist(self.spotify_user_id, name)
        return self.playlist_id
    
    def add_tracks_to_spotify(self):
        self.tracks_ids = []
        self.playlist.add_tracks(self.youtube.videos)
        return self.tracks_ids


if __name__ == "__main__":
    youtube_url = input("🔗 Entrez l'URL de la playlist YouTube : ")
    spotify_user_id = input("🎵 Entrez votre Spotify user ID : ")

    sync = Synchronizer(youtube_url, spotify_user_id)
    sync.extract_youtube()
    sync.create_spotify_playlist()
    sync.add_tracks_to_spotify()


# if __name__ == "__main__":
#     playlist_url = "https://www.youtube.com/playlist?list=PL0C00MH_AB4eundtu0PqswbWyYHdZawZi"
#     playlist_id = yt.extract_playlist_id(playlist_url) # extraire l'ID de la playlist depuis l'URL

#     videos = yt.get_videos(playlist_id)
#     titles = yt.get_titles(videos)
#     artists = yt.get_artists(videos)

#     print("Titles:", titles)
