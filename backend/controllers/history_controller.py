from flask import jsonify, session
from backend.sql_models.sync_run import SyncRun

def history_list():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    runs = (SyncRun.query
            .filter_by(user_id=user_id)
            .order_by(SyncRun.started_at.desc())
            .limit(20)
            .all())

    return jsonify([{
        "id": r.id,
        "job_id": r.job_id,
        "status": r.status,
        "started_at": r.started_at.isoformat(),
        "ended_at": r.ended_at.isoformat() if r.ended_at else None,
        "added": r.added,
        "skipped": r.skipped,
        "failed": r.failed,
    } for r in runs]), 200