import requests
import json
from flask import Flask, render_template
import config
from pyfy import Spotify

app = Flask(__name__)
#app.config.from_object('config')

#client_id = config.client_id
spt = Spotify('BQAKB6dyRzkak2ebEw0QGfjInAtFiH5nWf751_d3B0Cf2s1K-EM2etnkK1erLaC9v2rM4EJ5XexzhJ5loJRTkH6y11ZdNut6BvLy4BBOnjJjWH3nKggqZxmSF6O71w_M4C13hdrAElNZNhAj1qByKxfiprefx9LeuslAtS76AWAORXfjZ5B7uV0Z6YgAmyS_XBMcnd5gGFm5RUvcveyQelcEdMK50aqJ5Bc7FBYKHOABVeHbGYb6oz0qlocECoxQpLuCitWvgB5-QoiSal4')


@app.route('/')
@app.route('/index')
def home():
    return render_template('home.html')

@app.route('/add')
def add():
    return "hello world"
    
@app.route('/queue')
def queue():
    data = []
    results = spt.playlist_tracks(playlist_id="55UelCQIRMlZhVEKGSyUOU", fields="items(track(name,album(name),artists.name))")
    for song in results["items"]:
        entry = {"title": song["track"]["name"], "artist": song["track"]["artists"][0]["name"], "album":  song["track"]["album"]["name"]}
        data.append(entry)
        
    return render_template('queue.html', x=data)
    
@app.route('/recent')
def recent():
    return render_template('recent.html')
    
def addTrackToPlaylist(token, user, playlist_id, track_id, position):
    track = 'spotify:track:' + track_id
    auth = 'Bearer' + token
    url = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks'
    headers = {'Authorization': auth}
    payload = {'position': position, 'uris': track}
    post = requests.post(url, headers=headers, data=json.dumps(payload))

if __name__ == '__main__':
    app.run()