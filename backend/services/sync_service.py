# Logique métier pour la synchronisation YouTube vers Spotify
from config import SPOTIFY_USER_ID
from backend.main import Synchronizer
from dotenv import load_dotenv
from backend.models.spotify_model import SPOTIFY_USER_ID


def synchronize_youtube_to_spotify(youtube_url):
    """Service : synchronise une playlist YouTube vers Spotify"""
    sync = Synchronizer(youtube_url, SPOTIFY_USER_ID) # Initialisation du synchroniseur
    sync.extract_youtube() # Extraction des données YouTube
    sync.create_spotify_playlist() # Création de la playlist Spotify
    sync.add_tracks_to_spotify() # Ajout des morceaux à la playlist Spotify
    
    return {
        "message": f"Playlist '{sync.playlist_name}' synchronisée !",
        "nb_tracks_added": len(sync.track_ids), 
        "playlist_name": sync.playlist_name
    }