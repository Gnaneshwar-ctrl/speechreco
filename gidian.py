import datetime
import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing")
            query = r.recognize_google(audio, 'en=US')
            print(query)
        except Exception as e:
            print(e)
            speak("say that again")

            return "None"
        return query

if __name__ == "__main__":
    query = input().lower()
    print(query)