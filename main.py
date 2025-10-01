from app.models.youtube_model import get_videos, get_titles, get_artists

if __name__ == "__main__":
    playlist_id = "PL0C00MH_AB4eundtu0PqswbWyYHdZawZi"
    videos = get_videos(playlist_id)
    titles = get_titles(videos)
    artists = get_artists(videos)

    print("🎵 Titres :", titles)
    print("👤 Artistes :", artists)
