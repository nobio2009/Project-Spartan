import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Spotify stuff
username = 's9ulz0uh2m3yu6etr11am2fi4'
client_id = '289448ca74fe4e45aa385f5b962299fc'
client_secret = '91dd8f877c914ee69c7c5d3c70440921'
redirect_url = 'http://localhost:2009/'

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-recently-played"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret= client_secret, redirect_uri=redirect_url, scope=scope))

results = sp.current_user_recently_played()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])