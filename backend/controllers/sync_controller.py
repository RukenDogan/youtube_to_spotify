from flask import request, jsonify, redirect, session
from backend.services.sync_service import synchronize_youtube_to_spotify
import os
from spotipy.oauth2 import SpotifyOAuth


# Configuration Spotify
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
SCOPE = "playlist-modify-public playlist-modify-private"

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=SCOPE
)


# Routes Spotify
def spotify_login():
    """Redirige l'utilisateur vers Spotify pour autorisation"""
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


def spotify_callback():
    """Récupère le code Spotify et génère le token"""
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "Missing code"}), 400

    token_info = sp_oauth.get_access_token(code, check_cache=False)
    session['spotify_token'] = token_info

    # Redirige vers le frontend (Dashboard)
    return redirect("http://localhost:5173/dashboard")


def get_token():
    """Renvoie le token Spotify stocké en session"""
    token_info = session.get("spotify_token")
    if not token_info:
        return jsonify({"error": "No token"}), 401
    return jsonify({"access_token": token_info["access_token"]})



# Synchronisation YouTube - Spotify
def sync_playlist():
    """Contrôleur Flask pour la synchronisation"""
    data = request.json
    youtube_url = data.get("youtube_url")

    if not youtube_url:
        return jsonify({"error": "URL YouTube manquante"}), 400

    try:
        result = synchronize_youtube_to_spotify(youtube_url)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
