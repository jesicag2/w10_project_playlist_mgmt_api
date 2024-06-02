from flask import Flask, request, jsonify
from manager import PlaylistManager

app = Flask(__name__)
playlist_manager = PlaylistManager()

@app.route('/playlist/create', methods=['POST'])
def create_playlist():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    playlist_id = playlist_manager.create_playlist(name, description)
    return jsonify({'message': 'Playlist created successfully', 'playlist_id': playlist_id}), 201


@app.route('/')
def index():
    return 'Welcome to my simple Playlist Manager API :)'

@app.route('/playlist/<int:playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    playlist = playlist_manager.get_playlist(playlist_id)
    if playlist is None:
        return jsonify({'error': 'Playlist not found'}), 404
    return jsonify({'playlist_id': playlist.playlist_id, 'name': playlist.name, 'description': playlist.description, 'songs': [song.__dict__ for song in playlist.songs]}), 200

@app.route('/playlist/update/<int:playlist_id>', methods=['PUT'])
def update_playlist(playlist_id):
    data = request.json
    name = data.get('name')
    description = data.get('description')
    success = playlist_manager.update_playlist(playlist_id, name, description)
    if not success:
        return jsonify({'error': 'Playlist not found'}), 404
    return jsonify({'message': 'Playlist updated successfully', 'playlist_id': playlist_id}), 200

@app.route('/playlist/delete/<int:playlist_id>', methods=['DELETE'])
def delete_playlist(playlist_id):
    success = playlist_manager.delete_playlist(playlist_id)
    if not success:
        return jsonify({'error': 'Playlist not found'}), 404
    return jsonify({'message': 'Playlist deleted successfully', 'playlist_id': playlist_id}), 200

@app.route('/playlist/<int:playlist_id>/add_song', methods=['POST'])
def add_song_to_playlist(playlist_id):
    data = request.json
    title = data.get('title')
    artist = data.get('artist')
    album = data.get('album')
    genre = data.get('genre')
    song_id = playlist_manager.add_song_to_playlist(playlist_id, title, artist, album, genre)
    if not song_id:
        return jsonify({'error': 'Playlist not found'}), 404
    return jsonify({'message': 'Song added to playlist successfully', 'song_id': song_id}), 201

@app.route('/playlist/<int:playlist_id>/remove_song/<int:song_id>', methods=['DELETE'])
def remove_song_from_playlist(playlist_id, song_id):
    success = playlist_manager.remove_song_from_playlist(playlist_id, song_id)
    if not success:
        return jsonify({'error': 'Song not found in playlist'}), 404
    return jsonify({'message': f'Song with ID {song_id} removed from playlist'}), 200

if __name__ == '__main__':
    app.run(debug=True)
