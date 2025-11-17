import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pathlib import Path


dotenv_path = Path(__file__).resolve().parent.parent.parent / ".env.local"
print("Chemin du .env.local :", dotenv_path)
print("Existe :", dotenv_path.exists())

load_dotenv(dotenv_path=dotenv_path)

# récupérer l'URI
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("MONGO_URI n'est pas défini ! Vérifie .env.local à la racine du projet")

# connexion à la base
db = MongoClient(MONGO_URI)["beatsync"]

# test simple pour vérifier la connexion
try:
    print("Collections existantes :", db.list_collection_names())
    print("✅ MongoDB connecté !")
except Exception as e:
    print("❌ Impossible de se connecter à MongoDB :", e)
