# Route principal de l'application Flask
from doctest import debug

from config import FLASK_SECRET_KEY, FRONTEND_URL, DATABASE_URL
from flask import Flask
from flask_cors import CORS
from controllers.sync_controller import (sync_playlist, spotify_login, spotify_callback, get_token)
import os
from flask_migrate import Migrate
from db import db
# Import des modèles SQLAlchemy afin que Alembic puisse les détecter pour les migrations
from sql_models.user import User
from sql_models.sync_job import SyncJob
from sql_models.sync_run import SyncRun

from controllers.history_controller import history_list, history_detail
from controllers.sync_controller import debug_session


app = Flask(__name__) # Création de l'application Flask
app.secret_key = FLASK_SECRET_KEY # Clé secrète pour les sessions Flask

# Configuration de la base de données SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Connexion à la base de données
db.init_app(app)

# Migrations
migrate = Migrate(app, db)

# CORS pour autoriser les appels des routes depuis l'URL frontend
# CORS(app, origins=[FRONTEND_URL], supports_credentials=True)
origins = [FRONTEND_URL.rstrip("/")] if FRONTEND_URL else []
CORS(app, origins=origins, supports_credentials=True)

# Routes de l'historique
app.add_url_rule("/history", view_func=history_list, methods=["GET"])
app.add_url_rule("/history/<int:run_id>", view_func=history_detail, methods=["GET"])

# Routes de débogage
app.add_url_rule("/debug-session", view_func=debug_session, methods=["GET"])

# Routes Spotify
app.add_url_rule("/login", view_func=spotify_login)
app.add_url_rule("/callback", view_func=spotify_callback)
app.add_url_rule("/token", view_func=get_token, methods=["GET"])

# Route de synchronisation
app.add_url_rule("/youtube-to-spotify", view_func=sync_playlist, methods=["POST"])


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=debug)