import requests
import json
from pyfy import Spotify

def test():
    auth = 'Bearer ' + 'BQAvYirJ_xDP9bqg1G4M4fb3yncqdU8KCFTb_69ag-xCw6sgF9lN6qXy3XCjpmsOfcyiKTmWAN8oZsVV8xnJoNapsshN-O7iKv5vB1C49d-rjgrO7CtF9tCEA0REBvaqa_1c4PFJyIWlYN0FizAB8hvqTNDGAMdJzmq90CiuAnw_yqjxbPwamo6CeCHXM9GopWwOgJ3JJ3IqXvEV341EqFx6U0gKrrir9BJCuXugU-wRFfS5OWCTCm7TFoqFdJcce_P-nPuJkJmuZ49pmb4'
    url =  'https://api.spotify.com/v1/playlists/55UelCQIRMlZhVEKGSyUOU/tracks?fields=items(track(name,album(name),artists.name))'
    headers = {'Authorization': auth,'Content-Type': 'application/json'}
    #payload = {'fields': 'items(track(name,album(name),artists.name))'}
    payload = {}
    get = requests.get(url, headers=headers, data=json.dumps(payload))
    print(get.status_code)
    print(get.content)
    
test()
    