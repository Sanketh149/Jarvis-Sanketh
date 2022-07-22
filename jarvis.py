from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def hearMe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said:{query}\n")
    except Exception as e:
        print("Can you repeat please??")
        return None
    return query


def wishMe():
    speak("Hello I am sanketh's Jarvis version 1.0")
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sanketh!!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sanketh!!")
    else:
        speak("Good Evening Sanketh!!")


if __name__ == "__main__":
    wishMe()
    while True:
        query = hearMe().lower()

        if "my portfolio" in query:
            webbrowser.open("https://sanketh-portfolio.netlify.app")

        if "wikipedia" in query:
            speak("Searching For Results..Please Wait")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Sanketh According to wikipedia..")
            print(results)
            speak(results)
