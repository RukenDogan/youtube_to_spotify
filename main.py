from app.models import youtube_model as yt


if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=PL0C00MH_AB4eundtu0PqswbWyYHdZawZi"
    playlist_id = yt.extract_playlist_id(playlist_url) # extraire l'ID de la playlist depuis l'URL

    videos = yt.get_videos(playlist_id)
    titles = yt.get_titles(videos)
    artists = yt.get_artists(videos)

    print("Titles:", titles)
