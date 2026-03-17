import os
from dotenv import load_dotenv

# SKIP_ENV_CHECK = os.getenv("SKIP_ENV_CHECK") == "1"

# Chemin absolu vers la racine du projet
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENV_LOCAL = os.path.join(BASE_DIR, ".env.local")
ENV_DEFAULT = os.path.join(BASE_DIR, ".env")


# Charger les fichiers .env uniquement en local
# Sur Render, utilise uniquement les variables définies dans l'interface Render
if os.getenv("RENDER") is None:
    if os.path.exists(ENV_DEFAULT):
        load_dotenv(ENV_DEFAULT)

    if os.path.exists(ENV_LOCAL):
        load_dotenv(ENV_LOCAL, override=True)

# Variables d'environnement
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
# SPOTIFY_USER_ID = os.getenv("SPOTIFY_USER_ID")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
# MONGO_URI = os.getenv("MONGO_URI")
DATABASE_URL = os.getenv("DATABASE_URL")
FRONTEND_URL = os.getenv("FRONTEND_URL", "")

# Compatibilité PostgreSQL
if DATABASE_URL:
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)
    elif DATABASE_URL.startswith("postgresql://"):
        DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)


# Vérification
required_vars = {
    "YOUTUBE_API_KEY": YOUTUBE_API_KEY,
    "SPOTIFY_CLIENT_ID": SPOTIFY_CLIENT_ID,
    "SPOTIFY_CLIENT_SECRET": SPOTIFY_CLIENT_SECRET,
    "SPOTIFY_REDIRECT_URI": SPOTIFY_REDIRECT_URI,
    # "SPOTIFY_USER_ID": SPOTIFY_USER_ID,
    "FLASK_SECRET_KEY": FLASK_SECRET_KEY,
    # "MONGO_URI": MONGO_URI,
    "DATABASE_URL": DATABASE_URL,
    "FRONTEND_URL": FRONTEND_URL,
}

missing = [name for name, value in required_vars.items() if not value]

# if missing and not SKIP_ENV_CHECK:
#     raise RuntimeError(...)

if missing:
    raise RuntimeError(f"Variables manquantes : {', '.join(missing)}")