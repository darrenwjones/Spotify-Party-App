import requests
import json
from flask import Flask, render_template
import config

app = Flask(__name__)
#app.config.from_object('config')

#client_id = config.client_id

@app.route('/')
def home():
    return render_template('home.html')

def addTrackToPlaylist(token, user, playlist_id, track_id, position):
    track = 'spotify:track:' + track_id
    auth = 'Bearer' + token
    url = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks'
    headers = {'Authorization': auth}
    payload = {'position': position, 'uris': track}
    post = requests.post(url, headers=headers, data=json.dumps(payload))

if __name__ == '__main__':
    app.run()