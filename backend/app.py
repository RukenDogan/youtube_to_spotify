# Route principal de l'application Flask
from flask import Flask
from flask_cors import CORS
import os
from backend.controllers.sync_controller import (sync_playlist, spotify_login, spotify_callback, get_token)

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5173"], supports_credentials=True)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev_secret")

# Routes Spotify
app.add_url_rule("/login", view_func=spotify_login)
app.add_url_rule("/callback", view_func=spotify_callback)
app.add_url_rule("/token", view_func=get_token, methods=["GET"])

# Route de synchronisation
app.add_url_rule("/youtube-to-spotify", view_func=sync_playlist, methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)
