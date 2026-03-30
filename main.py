import speech_recognition as sr
import pyttsx3
import webbrowser
import ollama  as ol
import threading



r = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=7)
        print("Speak...")
        audio = r.listen(source, phrase_time_limit=6)
        

    try:
        text_recognize = r.recognize_google(audio).lower()
        print("You said:", text_recognize)
        return handle_command(text_recognize)
        

    except sr.UnknownValueError:
        print("Could not understand audio.")
        speak("Sorry, I could not understand.")
    except sr.RequestError as content:
        print("API error:", content)
        speak("Speech service error.")
    return True



def handle_command(command: str):
    if "hello" in command:
        speak("Hello! How can I help?")
        return True

    elif "open youtube" in command:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
        return True

    elif "play music" in command:
        speak("Playing music on spotify.")
        webbrowser.open("https://open.spotify.com/collection/tracks")
        return True
    
    elif "open instagram" in command:
        speak("Opening Instagram.")
        webbrowser.open("https://www.instagram.com")
        return True
    
    elif "open WhatsApp" in command:
        speak("Opening Whatsapp.")
        webbrowser.open("https://www.whatsapp.com")
        return True


    elif "exit" in command or "quit" in command:
        speak("Goodbye")
        return False
     
    else:
        response = generate_response(command)
        speak(response)
        print()
        return True
    
def generate_response(ai_text_recognize: str) -> str:
    response = ol.chat(
        model='gpt-oss:120b-cloud',
        messages=[
            {'role': 'system', 'content': "(You may respond only in English. Do not use any other language)"},
            {'role': 'user', 'content': ai_text_recognize}
        
        ],
        stream=True,
        options={"temperature": 0.4}
    )
    response_text = ""
    for chunk in response:
        
        response_text += chunk["message"]["content"]
        print(chunk["message"]["content"],end="", flush=True)
    print()
    return response_text



def speak(text_recognize: str):
    def _speak():
        content = pyttsx3.init()
        content.say(text_recognize)
        content.runAndWait()
        del content
    
    t = threading.Thread(target=_speak)
    t.start()
    t.join()




if __name__ == "__main__":
    print("Starting voice assistant...")
    try:
        while listen():
            pass
    except KeyboardInterrupt:
        print("Exiting...")
        speak("Goodbye.")

