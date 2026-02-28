# récupérer les vidéos d’une playlist
from config import YOUTUBE_API_KEY
import re # pour les opérations sur les chaînes de caractères
from googleapiclient.discovery import build # pour interagir avec l'API YouTube
from urllib.parse import urlparse, parse_qs # pour extraire l'ID de la playlist depuis l'URL


# extraire l'ID de la playlist depuis l'URL
def extract_playlist_id(url): # extraire l'ID de la playlist depuis l'URL
    query = urlparse(url).query # analyser l'URL pour extraire la partie de l'URL qui contient l'ID de la playlist
    params = parse_qs(query) # analyser la chaîne de requête pour extraire les paramètres
    return params["list"][0] if "list" in params else None # retourner l'ID de la playlist


# récupérer les informations de la playlist
def get_playlist_info(playlist_id):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.playlists().list(
        part="snippet",
        id=playlist_id
    )
    response = request.execute()
    if response['items']:
        snippet = response['items'][0]['snippet']
        title = snippet['title']
        channel_title = snippet['channelTitle']
        channel_title = re.sub(r"\s*-\s*topic$", "", channel_title, flags=re.IGNORECASE).strip()
        return title, channel_title
    return None, None


# récupérer les vidéos d'une playlist
def get_videos(playlist_url):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY) # construire le service YouTube avec la clé API
    
    videos = [] # liste pour stocker les IDs des vidéos
    next_page_token = None # token de la page suivante

    while True:
        request = youtube.playlistItems().list( # récupérer les vidéos
            part="snippet", # les informations de la vidéo
            playlistId=playlist_url, # utiliser l'ID de la playlist
            maxResults=50, # maximum autorisé par l'API
            pageToken=next_page_token # le token de la page suivante
        )
        response = request.execute() # exécuter la requête
    
        for item in response.get('items', []): # parcourir les éléments de la réponse
            video_id= item['snippet']['resourceId']['videoId']
            videos.append(video_id) # ajouter l'ID de la vidéo à la liste
    
        # Pagination pour récupérer toutes les vidéos
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    print(f"Total vidéos récupérées : {len(videos)}")
    return videos


# récupérer les titres des vidéos
def get_titles(videos):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    titles = []

    for i in range(0, len(videos), 50):
        batch = videos[i:i+50]
        request = youtube.videos().list(part="snippet", id=",".join(batch))
        response = request.execute()

        for item in response.get("items", []):
            titles.append(item["snippet"]["title"])

    return titles
# def get_titles(videos):
#     youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY) # construire le service YouTube avec la clé API
#     request = youtube.videos().list(part="snippet", id=",".join(videos)) # récupérer les informations des vidéos
#     response = request.execute() # exécuter la requête
#     titles = [] # liste pour stocker les titres des vidéos
#     for item in response['items']: # parcourir les éléments de la réponse
#         titles.append(item['snippet']['title']) # ajouter le titre de la vidéo à la liste
#     return titles # retourner la liste des titres des vidéos


# récupérer les artistes des vidéos
def get_artists(videos):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    artists = []

    for i in range(0, len(videos), 50):
        batch = videos[i:i+50]
        request = youtube.videos().list(part="snippet", id=",".join(batch))
        response = request.execute()

        for item in response.get("items", []):
            channel_title = item["snippet"]["channelTitle"]
            channel_title = re.sub(
                r"(\s*-\s*topic$)|(\s*\(.*official.*\)$)",
                "",
                channel_title,
                flags=re.IGNORECASE
            ).strip()
            artists.append(channel_title)

    return artists

# def get_artists(videos):
#     youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY) # construire le service YouTube avec la clé API
#     request = youtube.videos().list(part="snippet", id=",".join(videos)) # récupérer les informations des vidéos
#     response = request.execute() # exécuter la requête
#     artists = [] # liste pour stocker les artistes des vidéos
#     for item in response['items']: # parcourir les éléments de la réponse
#         channel_title = item['snippet']['channelTitle']
#         channel_title = re.sub(r"(\s*-\s*topic$)|(\s*\(.*official.*\)$)", "", channel_title, flags=re.IGNORECASE).strip()
#         artists.append(channel_title) # ajouter le nom de la chaîne (artiste) à la liste
#     return artists # retourner la liste des artistes des vidéos




# if __name__ == "__main__":
#     playlist_url = "https://www.youtube.com/playlist?list=PL0C00MH_AB4eundtu0PqswbWyYHdZawZi"
#     playlist_id = extract_playlist_id(playlist_url) # extraire l'ID de la playlist depuis l'URL

#     videos = get_videos(playlist_id)
#     titles = get_titles(videos)
#     artists = get_artists(videos)
#     print(titles)

