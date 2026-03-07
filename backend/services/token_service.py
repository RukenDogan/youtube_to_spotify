from services.mongo_tokens import get_spotify_token, save_spotify_token
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI
from spotipy.oauth2 import SpotifyOAuth
import time

SCOPE = "playlist-modify-public playlist-modify-private"

def _sp_oauth() -> SpotifyOAuth:
    return SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=SCOPE
)

def get_valid_access_token(spotify_user_id: str) -> str | None: # récupère un token valide
    doc = get_spotify_token(spotify_user_id) # récupère le token
    if not doc: # pas de token
        return None

    access_token = doc.get("access_token") # token d'accès
    refresh_token = doc.get("refresh_token") # token de rafraîchissement
    expires_at = doc.get("expires_at") # date d'expiration

    if expires_at and time.time() < (expires_at - 60): # 60s avant expiration
        return access_token

    if not refresh_token: # pas de refresh token
        return None

    # token_info = _sp_oauth.refresh_access_token(refresh_token) # refresh le token
    sp_oauth = _sp_oauth()
    token_info = sp_oauth.refresh_access_token(refresh_token) # refresh le token
    
    save_spotify_token( # sauvegarde le nouveau token
        spotify_user_id,
        access_token=token_info["access_token"],
        refresh_token=token_info.get("refresh_token") or refresh_token,
        expires_at=token_info["expires_at"],
    )
    return token_info["access_token"]