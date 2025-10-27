from backend.app import app

def test_youtube_to_spotify():
    client = app.test_client()
    
    response = client.post(
        "/youtube-to-spotify",
        json={"youtube_url": "https://www.youtube.com/playlist?list=PL0C00MH_AB4eundtu0PqswbWyYHdZawZi"}
    )
    
    # vérifier que la requête a réussi
    assert response.status_code == 200
    
    # vérifier que la réponse contient bien 'playlist_name'
    data = response.get_json()
    assert "playlist_name" in data
    assert "nb_tracks_added" in data
