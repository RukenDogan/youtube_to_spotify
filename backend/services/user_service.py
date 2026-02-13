from backend.db import db
from backend.sql_models.user import User

def get_or_create_user_by_spotify_id(spotify_user_id: str) -> User:
    user = User.query.filter_by(spotify_user_id=spotify_user_id).first()
    
    if user:
        return user

    user = User(spotify_user_id=spotify_user_id)
    db.session.add(user)
    db.session.commit()
    
    return user