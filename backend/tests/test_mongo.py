from backend.utils.mongo import db

# Example test to check connection and list collections
print(db.list_collection_names())
