from flask import Flask, request, jsonify
from models.spotify_model import 
from models.youtube_model import

app = Flask(__name__)

@app.route("/youtube-to-spotify", methods=["POST", "GET"])
def sync_playlist():
    if request.method == "POST":
        data = request.json
        youtube_url = data.get("youtube_url")
        # ici tu appelleras tes fonctions Python pour créer la playlist sur Spotify
        result = {"message": f"Playlist de {youtube_url} synchronisée !"}
        return jsonify(result)
    else:
        return jsonify({"message": "Methode non supportée"})
