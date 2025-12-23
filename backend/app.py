# Route principal de l'application Flask
from config import FLASK_SECRET_KEY, FRONTEND_URL
from flask import Flask
from flask_cors import CORS
from backend.controllers.sync_controller import (sync_playlist, spotify_login, spotify_callback, get_token)
import os

app = Flask(__name__)
CORS(app, origins=[FRONTEND_URL], supports_credentials=True)
app.secret_key = FLASK_SECRET_KEY

# Routes Spotify
app.add_url_rule("/login", view_func=spotify_login)
app.add_url_rule("/callback", view_func=spotify_callback)
app.add_url_rule("/token", view_func=get_token, methods=["GET"])

# Route de synchronisation
app.add_url_rule("/youtube-to-spotify", view_func=sync_playlist, methods=["POST"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
