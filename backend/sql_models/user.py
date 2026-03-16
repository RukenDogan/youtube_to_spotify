import uuid
from datetime import datetime, timezone
from db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    spotify_user_id = db.Column(db.String(64), unique=True, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                       default=lambda: datetime.now(timezone.utc),
                       nullable=False
    )
    access_token = db.Column(db.Text, nullable=True)
    refresh_token = db.Column(db.Text, nullable=True)
    expires_at = db.Column(db.BigInteger, nullable=True)