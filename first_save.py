import speech_recognition as sr
import pyttsx3
import webbrowser



r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text_recognize: str):
    engine.say(text_recognize)
    engine.runAndWait()

def handle_command(command: str):
    if "hello" in command:
        speak("Hello! How can I help?")

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    elif "play music" in command:
        speak("Playing music on spotify.")
        webbrowser.open("https://open.spotify.com/collection/tracks")

    elif "open instagram" in command:
        speak("Opening Instagram.")
        webbrowser.open("https://www.instagram.com")

    elif "exit" in command or "quit" in command:
        speak("Goodbye")
        return False
    
    else:
        speak("You said " + command)
    return True


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        print("Speak...")
        audio = r.listen(source, phrase_time_limit=6)
        
    try:
        text_recognize = r.recognize_google(audio).lower()
        print("You said:", text_recognize)
        return handle_command(text_recognize)


    except sr.UnknownValueError:
        print("Could not understand audio.")
        speak("Sorry, I could not understand.")
    except sr.RequestError as e:
        print("API error:", e)
        speak("Speech service error.")
    return True


if __name__ == "__main__":
    print("Starting voice assistant...")
    try:
        while listen():
            pass
    except KeyboardInterrupt:
        print("Exiting...")
        speak("Goodbye.")

