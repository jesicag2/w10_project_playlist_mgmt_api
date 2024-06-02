class Playlist:
    def __init__(self, playlist_id, name, description):
        self.playlist_id = playlist_id
        self.name = name
        self.description = description
        self.songs = []

class Song:
    def __init__(self, song_id, title, artist, album, genre):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre

class PlaylistManager:
    def __init__(self):
        self.playlists = {} 
        self.song_id_counter = 1  

    def create_playlist(self, name, description):
        playlist_id = len(self.playlists) + 1  
        playlist = Playlist(playlist_id, name, description)
        self.playlists[playlist_id] = playlist
        return playlist_id

    def get_playlist(self, playlist_id):
        if playlist_id not in self.playlists:
            return None
        playlist = self.playlists[playlist_id]
        return playlist

    def update_playlist(self, playlist_id, name, description):
        if playlist_id not in self.playlists:
            return False
        playlist = self.playlists[playlist_id]
        playlist.name = name
        playlist.description = description
        return True

    def delete_playlist(self, playlist_id):
        if playlist_id not in self.playlists:
            return False
        del self.playlists[playlist_id]
        return True

    def add_song_to_playlist(self, playlist_id, title, artist, album, genre):
        if playlist_id not in self.playlists:
            return False
        playlist = self.playlists[playlist_id]
        song_id = self.song_id_counter
        song = Song(song_id, title, artist, album, genre)
        playlist.songs.append(song)
        self.song_id_counter += 1 
        return song_id

    def remove_song_from_playlist(self, playlist_id, song_id):
        if playlist_id not in self.playlists:
            return False
        playlist = self.playlists[playlist_id]
        for song in playlist.songs:
            if song.song_id == song_id:
                playlist.songs.remove(song)
                return True
        return False
