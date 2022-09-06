import pyttsx3 #for text-to-speech conversion
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib #client session object that can be used to send mail to any internet machine 

engine = pyttsx3.init('sapi5') #to take voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

'''
Speak fuction will pronounce the string which is passed to it
'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

'''
wishMe will wish GM/GA/GE 
'''
def wishMe():
    speak("Initializing JARVIS...")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!!!")
    else:
        speak("Good Evening!!!")
    speak("I am Jarvis Sir. Please Tell Me How Can I Help You.")


'''
takeCommand takes microphone input from the user and returns string output
'''
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


wishMe()
while True:
    query= takeCommand().lower()

    # logic on executing tasks based on query
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query,sentences=2)
        speak("According To Wikipedia   ")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.get('C://Program Files//Google//Chrome//Application//chrome.exe %s').open("youtube.com")

    elif 'open google' in query:
        webbrowser.get('C://Program Files//Google//Chrome//Application//chrome.exe %s').open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.get('C://Program Files//Google//Chrome//Application//chrome.exe %s').open("stackoverflow.com")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")

    elif 'open vs code' in query:
        codePath = "C:\\Users\\Keshav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'deactivate jarvis' or 'exit' in query:
        speak("Deactivating jarvis....")
        speak("Jarvis Deactivated")
        print("Jarvis Deactivated.")
        break