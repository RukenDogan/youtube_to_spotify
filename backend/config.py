import os
from dotenv import load_dotenv

# Chemin absolu vers la racine du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV_LOCAL = os.path.join(BASE_DIR, ".env.local")
ENV_DEFAULT = os.path.join(BASE_DIR, ".env")

if os.path.exists(ENV_LOCAL):
    load_dotenv(ENV_LOCAL)
elif os.path.exists(ENV_DEFAULT):
    load_dotenv(ENV_DEFAULT)

# Variables d'environnement
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
SPOTIFY_USER_ID = os.getenv("SPOTIFY_USER_ID")

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev_secret")
MONGO_URI = os.getenv("MONGO_URI")
FRONTEND_URL = os.getenv("FRONTEND_URL")

# Vérification
required_vars = [
    YOUTUBE_API_KEY,
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET,
    SPOTIFY_REDIRECT_URI,
    SPOTIFY_USER_ID,
    MONGO_URI,
    FRONTEND_URL,
]

if not all(required_vars):
    raise RuntimeError("❌ Une ou plusieurs variables d'environnement ne sont pas définies !")
