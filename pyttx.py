import pyttsx3
import threading

def speak(text_recognize: str):
    def _speak():
        e = pyttsx3.init()
        e.say(text_recognize)
        e.runAndWait()
        del e
    
    t = threading.Thread(target=_speak)
    t.start()
    t.join()

# Test
for i in range(5):
    print(f"Speaking {i}")
    speak(f"Test number {i}")
    print(f"Done {i}")