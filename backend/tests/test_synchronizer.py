from backend.main import Synchronizer
from backend.models.spotify_model import SPOTIFY_USER_ID

def test_synchronizer():
    youtube_url = "https://www.youtube.com/playlist?list=PL0C00MH_AB4eundtu0PqswbWyYHdZawZi"
    sync = Synchronizer(youtube_url, SPOTIFY_USER_ID)
    sync.extract_youtube()
    sync.create_spotify_playlist()
    sync.add_tracks_to_spotify()

    assert len(sync.track_ids) > 0