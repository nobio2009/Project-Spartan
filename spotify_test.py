import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth


#Spotify stuff
username = 's9ulz0uh2m3yu6etr11am2fi4'
client_id = '289448ca74fe4e45aa385f5b962299fc'
client_secret = '91dd8f877c914ee69c7c5d3c70440921'
redirect_url = 'http://localhost:2009/'

scope = "user-read-playback-state, user-modify-playback-state"

client_credentials_manager = spotipy.SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret= client_secret, redirect_uri=redirect_url, scope=scope))
#print(sp.current_user_playing_track())

#sp.start_playback(device_id="cba73eb23bb1685c25db786af6cfe257")

#sp.pause_playback(device_id="cba73eb23bb1685c25db786af6cfe257")

#sp.transfer_playback(device_id="bef1871b37729a0ffc88b35af4b7c7a304427556", force_play=True)

#sp.add_to_queue("https://open.spotify.com/track/1xUZ6CgfpXspcQuEIOhf2v", None)

#sp.next_track(None)

#sp.previous_track(None)

#sp.track()

devices = sp.devices()

# Print the device information
#for device in devices['devices']:
#    print(f"Device ID: {device['id']}, Device Name: {device['name']}, Type: {device['type']}, Is Active: {device['is_active']}")

#musicData = sp.current_user_playing_track()
#songName = musicData['name']
#print(musicData['item']['name'])

spdevices = {'noah\'s room': 'cba73eb23bb1685c25db786af6cfe257', 'laptop': 'bef1871b37729a0ffc88b35af4b7c7a304427556'}

speach = "This is a sentence with laptop and room."

# Split the string into words
words = speach.split()
print(words)

device = None

for word in words:
    if word in spdevices:
        device = word
        print(device)
        break  # exit the loop once a valid device is found

if device is None:
    print('No valid device found in the sentence.')
else:
    print(f'Transferring playback to {device}')
    sp.transfer_playback(device_id=spdevices[device], force_play=True)
