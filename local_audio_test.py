import os
import random
import pygame

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
playing = False 
paused = False
while True:
    if not playing and not paused:
        # Start playing next random song
        current_song = os.path.join(folder, mp3s[current])
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
        playing = True
        
        
    pinput = input("Enter 'p' to pause/unpause, 's' to skip song: ")
    if pinput == 'p':
        if playing:
            pygame.mixer.music.pause()
            paused = True
        else:
            pygame.mixer.music.unpause()
        playing = not playing
    elif pinput == 's':
        # Skip to next song
        current += 1
        if current >= len(mp3s):
            current = 0
            playing = False
        
    # Check if song finished
    if not pygame.mixer.music.get_busy():
        playing = False
