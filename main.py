import speech_recognition as sr
import pyttsx3
import pywhatkit
import json
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import os
import random
import pygame

from data import *

#Voice recognition engine stuff
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Spotify stuff
sp_username = 's9ulz0uh2m3yu6etr11am2fi4'
client_id = '289448ca74fe4e45aa385f5b962299fc'
client_secret = '91dd8f877c914ee69c7c5d3c70440921'
redirect_url = 'http://localhost:2009/'

scope = "user-read-playback-state, user-modelify-playback-state"

client_credentials_manager = spotipy.SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret= client_secret, redirect_uri=redirect_url, scope=scope))

#Local music stuff
# Set up pygame mixer
pygame.mixer.init() 

# Get list of .mp3 files in folder
folder = "D:\Programming\Project-Spartan\local_music"
mp3s = [f for f in os.listdir(folder) if f.endswith(".mp3")]

# Shuffle list randomly 
random.shuffle(mp3s)

# Keep track of current song index
current = 0

# Main loop
playing = True
paused = True

#Random variables
first_time = True
spdevices = {'noah\'s room': 'cba73eb23bb1685c25db786af6cfe257', 'laptop': 'bef1871b37729a0ffc88b35af4b7c7a304427556'}

def say(_string):
    engine.say(_string)
    engine.runAndWait()
    
   
while True:
    try:
        if not playing and not paused:
            # Start playing next random song
            current_song = os.path.join(folder, mp3s[current])
            pygame.mixer.music.load(current_song)
            playing = True

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print('say something..')
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()

            print(text)

            if f'hey {AIname}' in text or f'ok {AIname}' in text:
                if text == f'hey {AIname}' or text == f'ok {AIname}':
                    if first_time == True:
                        say(f'Hello {username} i am {AIname} your personal ai')
                        first_time = False
                    else:
                        say(f'what can i do for you {username}')
                        audio = r.listen(source)
                        text = r.recognize_google(audio)
                        text = text.lower()

                string = text  
                split_string = string.split(' ')  
                new_string_list = split_string[0:][2:]
                command = ' '.join(new_string_list).lower()
                print(f'User: {username} tried to use command {command}')

                if 'say' in command:
                    string = text  
                    split_string = string.split(' ')  
                    new_string_list = split_string[3:]
                    speach = ' '.join(new_string_list).lower()
                    say(speach)

                elif 'identification' in command:
                    say(f'User: {username}, {userid} | AIC: {AIname}, {AIid}')

                #Internal systems/external circuitry/scripts
                elif 'load ' in command:
                    string = command 
                    split_string = string.split(' ')  
                    new_string_list = split_string[1:]
                    file = ' '.join(new_string_list).lower()

                    print(f'tried to load file {file}.py')
                    os.system(f'python scripts\{file}.py')

                #Spotify based commands
                elif 'play' in command:
                    sp.start_playback(device_id="bef1871b37729a0ffc88b35af4b7c7a304427556")

                elif 'pause' in command or 'shut up' in command:
                    sp.pause_playback(device_id="bef1871b37729a0ffc88b35af4b7c7a304427556")

                elif 'next song' in command:
                    sp.next_track(device_id="bef1871b37729a0ffc88b35af4b7c7a304427556")

                elif 'previous song' in command or 'go back a song' in command:
                    sp.previous_track(device_id="bef1871b37729a0ffc88b35af4b7c7a304427556")

                elif 'play on' in command:
                    # Split the string into words
                    words = command.split()
                    print(words)

                    device = None

                    for word in words:
                        if word in spdevices:
                            device = word
                            print(device)
                            break  # exit the loop once a valid device is found

                    if device is None:
                        print('No valid device found')
                        say('No valid device found')
                    else:
                        print(f'Transferring playback to {device}')
                        sp.transfer_playback(device_id=spdevices[device], force_play=True)

                elif 'what song is this' in command:
                    musicData = sp.current_user_playing_track()
                    songName = musicData['item']['name']
                    print(songName)

                    say(f'this song is called, {songName}')

                elif "local" in command:
                    if playing and paused:
                        pygame.mixer.music.unpause()
                        paused = False
                        playing = True
                    else:
                        pygame.mixer.music.play()
                        paused = True
                        playing = True
                
                elif "local p" in command:
                    if playing:
                        pygame.mixer.music.pause()
                        paused = True
                    else:
                        say('Nothing is playing')
                
                elif "local skip" in command:
                    # Skip to next song
                    current += 1
                    if current >= len(mp3s):
                        current = 0
                    playing = False

                if command == 'exit':
                    break
                    exit()
                    
            

    except KeyboardInterrupt:
        exit()

    except:
        print('say something..')
        r = sr.Recognizer()
        continue

exit()