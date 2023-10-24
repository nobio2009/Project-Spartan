import os

def speak():
    import pyttsx3

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.say(f'Hello world!')
    engine.runAndWait()


def search():
    try:
        from googlesearch import search
    except ImportError: 
        print("No module named 'google' found")
    
    # to search
    query = "titanfall 2"
    
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(j)

def slice():
    string = input('')
    first_word = string.split()[0]
    remaining_string = string[len(first_word):]
    print(remaining_string)


slice()