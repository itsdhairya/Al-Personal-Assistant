import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

print('Its - MY BOT')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
        print("Good morning")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
        print("Good afternoon")
    else:
        speak("Good evening!")
        print("Good evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"User said: {statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


def play_music():
    music_dir = 'C:\\Path\\To\\Your\\Music\\Directory'
    songs = os.listdir(music_dir)
    if songs:
        os.startfile(os.path.join(music_dir, songs[0]))
        speak("Playing music for you.")
    else:
        speak("No music files found in the directory.")


def open_code_editor():
    code_path = 'C:\\Path\\To\\Your\\Code\\Editor.exe'
    if os.path.exists(code_path):
        os.startfile(code_path)
        speak("Opening code editor.")
    else:
        speak("Code editor not found at the specified path.")


def take_note():
    speak("What should I write down?")
    note = takeCommand()
    if note != "None":
        with open('notes.txt', 'a') as f:
            f.write(note + '\n')
        speak("Note saved successfully!")


def read_notes():
    try:
        with open('notes.txt', 'r') as f:
            notes = f.readlines()
            if notes:
                speak("Here are your notes:")
                for note in notes:
                    speak(note)
            else:
                speak("No notes found.")
    except FileNotFoundError:
        speak("No notes found.")


speak("Bot Here, How can I assist you?")
wishMe()

if __name__ == '__main__':
    while True:
        speak("How can I help you?")
        statement = takeCommand().lower()

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Bot off')
            print('Bot off')
            break

        if 'open wikipedia' in statement:
            speak('Searching Wikipedia...')
            query = statement.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is available")
            time.sleep(5)

        # ... (continue with the previous commands)

        elif 'play music' in statement:
            play_music()

        elif 'open code' in statement:
            open_code_editor()

        elif 'take note' in statement:
            take_note()

        elif 'read notes' in statement:
            read_notes()

        elif 'launch website' in statement:
            speak("Sure, which website would you like to launch?")
            website = takeCommand().lower()
            if "google" in website:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google Chrome is open.")
            elif "youtube" in website:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("YouTube is open.")
            # Add more website options here.

        # ... (add more complex functionalities)

        time.sleep(3)
