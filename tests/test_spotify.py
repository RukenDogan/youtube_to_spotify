from app.models.youtube_model import extract_playlist_id

def test_extract_playlist_id():
    url = "https://www.youtube.com/playlist?list=PL123ABC"
    assert extract_playlist_id(url) == "PL123ABC"