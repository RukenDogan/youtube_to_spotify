# Route principal de l'application Flask
from config import FLASK_SECRET_KEY, FRONTEND_URL, DATABASE_URL
from flask import Flask
from flask_cors import CORS
from backend.controllers.sync_controller import (sync_playlist, spotify_login, spotify_callback, get_token)
import os
from backend.db import db
from backend.controllers.history_controller import history_list, history_detail
from backend.controllers.sync_controller import debug_session


app = Flask(__name__) # Création de l'application Flask
app.secret_key = FLASK_SECRET_KEY # Clé secrète pour les sessions Flask

# Configuration de la base de données SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

print("DB repr:", repr(DATABASE_URL))
print("DB len:", len(DATABASE_URL))
print("DB type:", type(DATABASE_URL))

# Routes de l'historique
app.add_url_rule("/history", view_func=history_list, methods=["GET"])
app.add_url_rule("/history/<int:run_id>", view_func=history_detail, methods=["GET"])

# Routes de débogage
app.add_url_rule("/debug-session", view_func=debug_session, methods=["GET"])

db.init_app(app)

with app.app_context():
    db.create_all()
print("Tables créées")


# CORS pour autoriser les appels des routes depuis l'URL frontend
CORS(app, origins=[FRONTEND_URL], supports_credentials=True)


# Routes Spotify
app.add_url_rule("/login", view_func=spotify_login)
app.add_url_rule("/callback", view_func=spotify_callback)
app.add_url_rule("/token", view_func=get_token, methods=["GET"])

# Route de synchronisation
app.add_url_rule("/youtube-to-spotify", view_func=sync_playlist, methods=["POST"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
