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
        "status": r.status,
        "started_at": r.started_at.isoformat(),
        "added": r.added,
        "failed": r.failed,
    } for r in runs]), 200

def history_detail(run_id: int):
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    run = SyncRun.query.filter_by(id=run_id, user_id=user_id).first()
    if not run:
        return jsonify({"error": "Not found"}), 404

    return jsonify({
        "id": run.id,
        "status": run.status,
        "started_at": run.started_at.isoformat(),
        "ended_at": run.ended_at.isoformat() if run.ended_at else None,
        "added": run.added,
        "failed": run.failed,
        "added_tracks": run.added_tracks or [],
        "failed_tracks": run.failed_tracks or [],
    }), 200