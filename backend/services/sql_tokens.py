from db import db
from sql_models.user import User


def save_spotify_token(
    spotify_user_id: str,
    access_token: str,
    refresh_token: str | None,
    expires_at: int,
) -> bool:
    try:
        user = User.query.filter_by(spotify_user_id=spotify_user_id).first()
        if not user:
            return False

        user.access_token = access_token
        user.refresh_token = refresh_token
        user.expires_at = expires_at
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print("PostgreSQL error while saving token:", e, flush=True)
        return False


def get_spotify_token(spotify_user_id: str) -> dict | None:
    try:
        user = User.query.filter_by(spotify_user_id=spotify_user_id).first()
        if not user or not user.access_token:
            return None

        return {
            "access_token": user.access_token,
            "refresh_token": user.refresh_token,
            "expires_at": user.expires_at,
        }
    except Exception as e:
        print("PostgreSQL error while fetching token:", e, flush=True)
        return None