import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import os 
import smtplib
import pyaudio
import wikipedia
import requests
import googlesearch

print("EDITH")
Master = "Firman"
listen = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello, good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good afternoon sir")
    else:
        speak("Hello, good evenning sir")
        speak("")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("recognizing..")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said : {query}\n")

    except Exception as e:
        print("sir can you said again please")
        query = None
    return query

speak("Hello Sir, im EDITH how can i help you")
wishMe()
query = take_command()
    
if "wikipedia" in query.lower():
    speak("let me check")
    query = query.replace("wikipedia","")
    result = wikipedia.summary(query,sentences=2)
    print(result)
    speak(result)
elif "play" in query.lower():
    song = query.replace("play","")
    speak ("playing"+song)
    pywhatkit.playonyt(song)
elif "open google" in query.lower():
    url = "google.com"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

elif "search" in query.lower():
    search = query.replace("search","")
    speak = (search+".com")
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(speak)
elif "introduce yourself" in query.lower():
    query = speak("my name is EDITH, abbreviation from Even dead im the hero")
    query = speak("im created by, firman wijaya kusuma")
    query = speak("I am assigned to be an assistant for firman wijaya kusuma ")
else:
    speak("not any intruction")
    print(take_command)
    
