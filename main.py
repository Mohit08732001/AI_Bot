import speech_recognition as sr
import webbrowser
import pywhatkit as kit

from Commands.chat import chat
from Commands.save_response import ai
from Commands.speaker import speak


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            q = r.recognize_google(audio, language="en-in")
            print(f"User said: {q}")
            return q
        except Exception as _:
            return "Some Error Occurred From Bot"


if __name__ == '__main__':
    speak("Hi I am a bot created using python, how may i help you today")
    while True:
        print("Listening")
        query = take_command()
        sites = [["youtube", "https://youtube.com"], ["google", "https://google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]}")
                webbrowser.open(site[1])
        if "on youtube".lower() in query.lower():
            speak("Sure")
            query.replace("on youtube", "")
            kit.playonyt(query)
        elif "Using artificial intelligence".lower() in query.lower():
            ai(content=query)
        elif "quit".lower() in query.lower():
            exit()
        else:
            chat(query)
