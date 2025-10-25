# Routes flask pour la synchronisation des playlists et le login Spotify

from flask import request, jsonify
from backend.services.sync_service import synchronize_youtube_to_spotify
from backend.models.spotify_model import SPOTIFY_USER_ID

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