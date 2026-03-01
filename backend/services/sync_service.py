# Logique métier pour la synchronisation YouTube vers Spotify
from models.synchronizer import Synchronizer
from services.token_service import get_valid_access_token

def synchronize_youtube_to_spotify(youtube_url, spotify_user_id):
    access_token = get_valid_access_token(spotify_user_id)
    if not access_token:
        raise RuntimeError("Token Spotify invalide ou expiré. Veuillez vous reconnecter.")
    
    sync = Synchronizer(youtube_url, spotify_user_id, access_token)
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