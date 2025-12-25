import os
from dotenv import load_dotenv

# chargement des variables d'environnement depuis le fichier .env.local
if os.path.exists(".env.local"):
    load_dotenv(".env.local")

# Variables d'environnement
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
SPOTIFY_USER_ID = os.getenv("SPOTIFY_USER_ID")

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev_secret")

MONGO_URI = os.getenv("MONGO_URI")

FRONTEND_URL = os.getenv("FRONTEND_URL")

# Vérification rapide
required_vars = [YOUTUBE_API_KEY, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, SPOTIFY_USER_ID, MONGO_URI]
if not all(required_vars):
    raise RuntimeError("❌ Une ou plusieurs variables d'environnement ne sont pas définies !")
