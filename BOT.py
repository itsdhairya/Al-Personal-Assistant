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
    if hour >= 0 and hour < 12:
        speak("ok BOT")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Go Ahead")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

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

speak("Bot Here How are you ?")
wishMe()

if __name__ == '__main__':

    while True:
        speak("How can I help you")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('BOt off')
            print('Bot off')
            break

        if 'open wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is available")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("City ??")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak("What City, Again ?")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('My name is Bot. I can communicate in english'
                  'I can open youtube, google chrome, gmail ,predict time, take a photo,search wikipedia,predict weather'
                  'in different cities , and get news!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Dhairya B")
            print("I was built by Dhairya B")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("There you go")

        elif 'news' in statement:
            news_url = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"
            response = requests.get(news_url)
            data = response.text
            news_data = json.loads(json.dumps(xmltodict.parse(data)))
            news_items = news_data['rss']['channel']['item']
            for idx, item in enumerate(news_items):
                if idx >= 5:
                    break
                speak(item['title'])
                
        elif "Camera coming up" in statement or "Take a picture" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'Search' in statement:
            statement = statement.replace("Search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'What do you know' in statement:
            speak('Search....')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("I shall shut the computer down... in 10 Seconds...")
            subprocess.call(["shutdown", "/l"])


        elif 'play music' in statement:
            play_music()

        elif 'open code' in statement:
            open_code_editor()

        elif 'take note' in statement:
            take_note()

        elif 'read notes' in statement:
            read_notes()


time.sleep(3)
