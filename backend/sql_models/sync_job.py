from datetime import datetime, timezone
from backend.db import db

class SyncJob(db.Model):
    __tablename__ = "sync_jobs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)

    youtube_playlist_id = db.Column(db.String(255), nullable=False)
    spotify_playlist_id = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
