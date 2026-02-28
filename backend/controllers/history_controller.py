from flask import jsonify, session
from sql_models.sync_run import SyncRun
from services.user_service import get_or_create_user_by_spotify_id

def history_list():
    spotify_user_id = session.get("spotify_user_id")
    if not spotify_user_id:
        return jsonify({"error": "Not authenticated"}), 401

    user = get_or_create_user_by_spotify_id(spotify_user_id)
    session["user_id"] = user.id
    user_id = user.id

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
        "playlist_title": r.job.youtube_playlist_title if r.job else "Unknown Playlist",
    } for r in runs]), 200


def history_detail(run_id: int):
    spotify_user_id = session.get("spotify_user_id")
    if not spotify_user_id:
        return jsonify({"error": "Not authenticated"}), 401

    user = get_or_create_user_by_spotify_id(spotify_user_id)
    session["user_id"] = user.id
    user_id = user.id

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
        "playlist_title": run.job.youtube_playlist_title if run.job else "Unknown Playlist",
    }), 200