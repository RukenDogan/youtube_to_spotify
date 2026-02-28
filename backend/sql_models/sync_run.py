from datetime import datetime, timezone
from db import db
from sqlalchemy.dialects.postgresql import JSON

class SyncRun(db.Model):
    __tablename__ = "sync_runs"

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey("sync_jobs.id"), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="RUNNING")
    started_at = db.Column(db.DateTime(timezone=True),
                       default=lambda: datetime.now(timezone.utc),
                       nullable=False)
    ended_at = db.Column(db.DateTime(timezone=True), nullable=True)
    added = db.Column(db.Integer, nullable=False, default=0)
    failed = db.Column(db.Integer, nullable=False, default=0)
    added_tracks = db.Column(JSON, nullable=True)
    failed_tracks = db.Column(JSON, nullable=True)

    # Relation vers SyncJob
    job = db.relationship("SyncJob", backref="runs")