from flask import Flask
from backend.controllers.sync_controller import sync_playlist

app = Flask(__name__)

app.add_url_rule("/youtube-to-spotify", view_func=sync_playlist, methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)
