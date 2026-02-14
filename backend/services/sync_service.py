# Logique métier pour la synchronisation YouTube vers Spotify
from backend.models.synchronizer import Synchronizer  # ou models/services/synchronizer

def synchronize_youtube_to_spotify(youtube_url, spotify_user_id):
    sync = Synchronizer(youtube_url, spotify_user_id)
    sync.extract_youtube()
    sync.create_spotify_playlist()
    sync.add_tracks_to_spotify()
    return {
        "message": f"Playlist '{sync.playlist_name}' synchronisée !",
        "nb_tracks_added": len(sync.track_ids),
        "playlist_name": sync.playlist_name,
    }
