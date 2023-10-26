import speech_recognition as sr
import pyttsx3
import pywhatkit
from googlesearch import search

from data import *

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

global first_time
first_time = False

def say(_string):
    engine.say(_string)
    engine.runAndWait()
    

                
while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print('say something..')
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()

            print(text)

            if f'hey {AIname}' in text:
                if text == f'hey {AIname}':
                    if first_time == True:
                        engine.say(f'Hello {username} i am {AIname} your personal ai')
                        engine.runAndWait()
                        first_time = False
                    else:
                        say(f'what can i do for you {username}')

                string = 'this is a string'  
                split_string = string.split(' ')  
                new_string_list = split_string[0:][2:]
                new_string = ' '.join(new_string_list)  
                print(new_string)
                    
            

    except KeyboardInterrupt:
        exit()

    except:
        print('say something..')
        r = sr.Recognizer()
        continue