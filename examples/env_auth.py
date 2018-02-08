# Shows the top artists for a user

import pprint
import sys
import os

import spotipy
import spotipy.util as util
import json

def auth_hook(token_info=None):
    if token_info:
        os.environ['SPOTIPY_TOKEN_INFO'] = json.dumps(token_info)
    if os.getenv('SPOTIPY_TOKEN_INFO'):
        return json.loads(os.getenv('SPOTIPY_TOKEN_INFO'))
    else:
        return None

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public  playlist-modify-private user-modify-playback-state user-read-playback-state'
token = util.prompt_for_user_token(username, scope, auth_hook=auth_hook)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_playlists(limit=50)
    for i, item in enumerate(results['items']):
        print("%d %s" %(i, item['name']))
else:
    print("Can't get token for", username)
