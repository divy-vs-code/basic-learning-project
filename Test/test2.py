import speech_recognition as sr
import webbrowser
import pyttsx3
import time

r = sr.Recognizer()
engine = pyttsx3.init()
time.sleep(1) 


print("loading...")
def speak(text):
    engine.say(text)   
    engine.runAndWait()

speak("Hello world")    # Queue something to speak3

