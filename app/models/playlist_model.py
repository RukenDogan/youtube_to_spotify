# créer des playlists et gérer les morceaux dedans
import datetime


class Playlist: # créer des playlists et gérer les morceaux dedans
    def __init__(self, name, description, public, tracks): # initialisation de l'instance Playlist
        self.name = name # nom de la playlist
        self.description = description # description de la playlist
        self.public = public # visibilité de la playlist (publique ou privée)
        self.tracks = tracks # liste des morceaux dans la playlist

    def add_track(self, track): # ajouter un morceau à la playlist
        self.tracks.append(track) # ajouter le morceau à la liste des morceaux de la playlist

    def add_tracks(self, tracks): # ajouter plusieurs morceaux à la playlist
        self.tracks.extend(tracks) # ajouter les morceaux à la liste des morceaux de la playlist

    def remove_track(self, track_list): # supprimer un morceau de la playlist
        self.tracks.remove(track_list) # supprimer le morceau de la liste des morceaux de la playlist

    def __repr__(self): # représentation de l'objet Playlist
        return f"Playlist(name={self.name}, description={self.description}, public={self.public}, tracks={self.tracks})" # représentation de l'objet Playlist avec ses attributs