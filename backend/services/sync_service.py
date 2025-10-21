from main import Synchronizer
from backend.models.spotify_model import SPOTIFY_USER_ID

def synchronize_youtube_to_spotify(youtube_url):
    """Service : synchronise une playlist YouTube vers Spotify"""
    sync = Synchronizer(youtube_url, SPOTIFY_USER_ID)
    sync.extract_youtube()
    sync.create_spotify_playlist()
    sync.add_tracks_to_spotify()
    
    return {
        "message": f"Playlist '{sync.playlist_name}' synchronisée !",
        "nb_tracks_added": len(sync.track_ids),
        "playlist_name": sync.playlist_name
    }
