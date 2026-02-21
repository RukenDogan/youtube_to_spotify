# Logique métier pour la synchronisation YouTube vers Spotify
from backend.models.synchronizer import Synchronizer  # ou models/services/synchronizer

def synchronize_youtube_to_spotify(youtube_url, spotify_user_id):
    sync = Synchronizer(youtube_url, spotify_user_id)
    sync.extract_youtube()
    sync.create_spotify_playlist()
    added_tracks, failed_tracks = sync.add_tracks_to_spotify()
    
    return {
        "message": f"Playlist '{sync.playlist_name}' synchronisée !",
        "playlist_name": sync.playlist_name,
        "spotify_playlist_id": sync.playlist_id,
        "nb_tracks_added": len(added_tracks),
        "nb_tracks_failed": len(failed_tracks),
        "added_tracks": added_tracks,
        "failed_tracks": failed_tracks,
    }