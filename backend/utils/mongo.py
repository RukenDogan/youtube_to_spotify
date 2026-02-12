from config import MONGO_URI
from pymongo import MongoClient
from pathlib import Path



# récupérer l'URI de MongoDB depuis les variables d'environnement
if not MONGO_URI:
    raise RuntimeError("MONGO_URI n'est pas défini ! Vérifie .env.local à la racine du projet")

# connexion à la base
db = MongoClient(MONGO_URI)["beatsync"]

# Collection pour stocker les tokens Spotify
tokens_collection = db["spotify_tokens"]


# test simple pour vérifier la connexion
try:
    print("Collections existantes :", db.list_collection_names())
    print("✅ MongoDB connecté !")
except Exception as e:
    print("❌ Impossible de se connecter à MongoDB :", e)

# fonctions pour gérer les tokens Spotify dans MongoDB
def save_spotify_token(spotify_user_id, access_token, refresh_token, expires_at):
    """
    Sauvegarde ou met à jour le token Spotify d'un utilisateur.
    """
    tokens_collection.update_one(
        {"spotify_user_id": spotify_user_id}, # filtre pour trouver le document correspondant
        {"$set": {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "expires_at": expires_at
        }},
        upsert=True # crée le document s'il n'existe pas
    )
    print(f"✅ Token enregistré pour {spotify_user_id}")

# fonction pour récupérer le token Spotify d'un utilisateur
def get_spotify_token(spotify_user_id):
    """
    Récupère le token Spotify d'un utilisateur depuis MongoDB.
    """
    doc = tokens_collection.find_one({"spotify_user_id": spotify_user_id})
    if doc:
        return doc
    else:
        return None

# save_spotify_token("test_user", "abc123", "def456", 1700000000)
# token = get_spotify_token("test_user")
# print("Token récupéré :", token)

