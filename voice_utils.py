# voice_utils.py
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 165)

def text_to_speech(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        pass

def speech_to_text(timeout=5, phrase_time_limit=7):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Speech recognition service unavailable."
