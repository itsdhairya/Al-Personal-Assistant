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


print('AA taro bhai - Bhailu ahiyaa')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Jai Shree ram, Kemcho")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Jai Shree ram, Kemcho subhh bapor")
        print("Hello,Good Afternoon")
    else:
        speak("Jai Shree ram, Kemcho subh ratrii")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Aagad Bol")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pharithi Bol...")
            return "None"
        return statement

speak("Bhailu Here su chaale Dhairya")
wishMe()


if __name__=='__main__':


    while True:
        speak("Sahheb su madad kari saku tamari")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Bhailu off')
            print('Bhailu off')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube kholiyu...")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome kholiyu...")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail kholiyu...")
            time.sleep(5)

        elif "weather su che" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("City ??")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
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
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('My name is Bhailu. I can talk in gujarati'
                  'I can open youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get news too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement or"Konne banayu tane" in statement:
            speak("I was built by Dhairya B")
            print("I was built by Dhairya B")
        
        # elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
        #     speak("I was built by Dhairya B")
        #     print("I was built by Dhairya B")

        # elif "open stackoverflow" in statement:
        #     webbrowser.open_new_tab("https://stackoverflow.com/login")
        #     speak("There you go")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('News tara screen per')
            time.sleep(6)

        elif "camera" in statement or "Photo le toh" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'sodh'  in statement:
            statement = statement.replace("sodh", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'su aavde tane' in statement:
            speak('Badhuj aavde tara bhai ne')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement:
            speak("10 Second ma bandh thai jase, Jai Shree Ram")
            subprocess.call(["shutdown", "/l"])

time.sleep(3)