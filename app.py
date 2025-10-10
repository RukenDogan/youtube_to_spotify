from flask import Flask, request, jsonify
from main import Synchronizer
from backend.models.spotify_model import SPOTIFY_USER_ID

app = Flask(__name__)

@app.route("/youtube-to-spotify", methods=["POST"])
def sync_playlist():
    data = request.json
    youtube_url = data.get("youtube_url")

    if not youtube_url:
        return jsonify({"error": "URL YouTube manquante"}), 400

    try:
        print("DEBUG: Création du Synchronizer")
        sync = Synchronizer(youtube_url, SPOTIFY_USER_ID)
        sync.extract_youtube()
        sync.create_spotify_playlist()
        sync.add_tracks_to_spotify()

        response = {
            "message": f"Playlist '{sync.playlist_name}' synchronisée !",
            "nb_tracks_added": len(sync.track_ids),
            "playlist_name": sync.playlist_name
        }
        return jsonify(response), 200

    except Exception as e:
        print("DEBUG: Erreur détectée", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)