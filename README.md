# Synchronisation de Playlists YouTube vers Spotify
---

## Description
---
Ce projet est une application Python qui permet de synchroniser les vidéos d'une playlist YouTube
en créant automatiquement une playlist correspondante sur Spotify.

L'objectif principal est de se familiariser avec :
- l'utilisation d'APIs REST (YouTube et Spotify),
- l'authentification OAuth,
- la gestion de données JSON,
- la structuration d'un projet en architecture MVC (Models, Controller, Views),
- la recherche intelligente de morceaux sur Spotify avec correspondance titre/artiste.

## Fonctionnalités
---
- Extraire les titres et artistes d'une playlist YouTube
- Créer une nouvelle playlist sur Spotify
- Rechercher les morceaux sur Spotify avec un score de correspondance
- Ajouter les morceaux trouvés à la playlist Spotify

## Prérequis
---
- Python 3.9 ou supérieur
- Un compte Spotify avec une application enregistrée pour obtenir Client ID et Client Secret
- Une clé API YouTube
- Modules Python :
    - spotipy
    - python-dotenv
    - google-api-python-client (pour YouTube)

## Installation
---
1. Cloner le projet :
   git clone <URL_DU_REPO>

2. Créer un environnement virtuel et l'activer :
   - python -m venv venv
   - source venv/bin/activate   # Linux/Mac
   - .\venv\Scripts\activate    # Windows
3. Installer les dépendances :
   - pip install -r requirements.txt
4. Créer un fichier `.env.local` avec :
   - SPOTIFY_CLIENT_ID=...
   - SPOTIFY_CLIENT_SECRET=...
   - SPOTIFY_REDIRECT_URI=...
   - SPOTIFY_USER_ID=...
   - YOUTUBE_API_KEY=...

## Utilisation
---
1. Lancer le script principal :
   python main.py
2. Entrer l'URL de la playlist YouTube quand demandé
3. L'application créera la playlist sur Spotify et ajoutera les morceaux trouvés

## Points importants
---
- Certains morceaux peuvent ne pas être trouvés si le nom ou l'artiste est trop différent
- Les vidéos YouTube provenant de chaînes "Topic" ou sans titre clair peuvent poser problème
- Ce projet est structuré selon une architecture MVC :
    - Models : youtube_model.py et spotify_model.py
    - Controller : prévu pour gérer la logique lorsque l'interface sera ajoutée
    - Views : à développer plus tard pour créer une interface utilisateur
- Le but est également de se préparer à l'ajout d'une interface graphique (par exemple avec Tkinter ou Flask/React)

---
Ruken