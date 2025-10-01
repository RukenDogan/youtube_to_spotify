# récupérer les vidéos d’une playlist
import os
from googleapiclient.discovery import build
from dotenv import load_dotenv


load_dotenv(dotenv_path=".env.local")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def get_videos(playlist_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.playlistItems().list(part="snippet", playlistId=playlist_id)
    response = request.execute()
    videos = []
    for item in response['items']:
        videos.append(item['snippet']['resourceId']['videoId'])
    return videos

# récupérer les titres des vidéos
def get_titles(videos):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.videos().list(part="snippet", id=",".join(videos))
    response = request.execute()
    titles = []
    for item in response['items']:
        titles.append(item['snippet']['title'])
    return titles

# récupérer les artistes des vidéos
def get_artists(videos):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.videos().list(part="snippet", id=",".join(videos))
    response = request.execute()
    artists = []
    for item in response['items']:
        artists.append(item['snippet']['channelTitle'])
    return artists


if __name__ == "__main__":
    playlist_id = "PL0C00MH_AB4eundtu0PqswbWyYHdZawZi"
    videos = get_videos(playlist_id)
    titles = get_titles(videos)
    artists = get_artists(videos)
    print(titles)

