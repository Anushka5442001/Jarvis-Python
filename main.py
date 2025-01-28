import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
from openai import OpenAI
from gtts import gTTS
import pygame  # Import the pygame library
import os
#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="be98137970c6423bb286623575b3ad62"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize the mixer module
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')  # Replace with your MP3 file path

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running while the music plays
    while pygame.mixer.music.get_busy():  # Check if the music is still playing
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
def aiProcess(command):
    client = OpenAI(
    api_key="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"
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        store=True,
        messages=[
            {"role": "system", "content": "You area virtual assistance named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]
        link = music_library.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=be98137970c6423bb286623575b3ad62")
        if r.status_code==200:
            #parse the JASON response
            data= r.json()

            #extract article
            articles = data.get('articles',[])

            #Print the Headlines
            for article in articles:
                speak(article['title'])
    else:
        #let OpenAI handle the request
       output= aiProcess(c)
       speak(output)



if __name__== "__main__":
    speak("Initialising Jarvis....")
    while True:
        #Listen to the wake word "Jarvis"

        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognising...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word= r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command= r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
