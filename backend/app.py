from flask import Flask
from backend.controllers.sync_controller import sync_playlist, spotify_login, spotify_callback
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"]) # autorise l'accès à l'API depuis l'URL http://localhost:5173

# Clé de sécurité pour sessions Flask
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev_secret")  # fallback si non définie

# Route pour l'authentification Spotify
app.add_url_rule("/login", view_func=spotify_login)

# Route pour la récupération du code Spotify
app.add_url_rule("/callback", view_func=spotify_callback)

# Route pour la synchronisation
app.add_url_rule("/youtube-to-spotify", view_func=sync_playlist, methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)
