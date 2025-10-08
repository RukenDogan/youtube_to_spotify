# test_youtube_models.py
from backend.models import youtube_model as yt

def test_extract_playlist_id():
    url = "https://www.youtube.com/playlist?list=PL0C00MH_AB4eundtu0PqswbWyYHdZawZi"
    result = yt.extract_playlist_id(url)
    assert result == "PL0C00MH_AB4eundtu0PqswbWyYHdZawZi"