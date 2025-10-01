import os
from dotenv import load_dotenv

# Priorité au .env.local si présent, sinon fallback sur .env
if os.path.exists(".env.local"):
    load_dotenv(".env.local")
else:
    load_dotenv(".env")

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")
