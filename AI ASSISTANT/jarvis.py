import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests

engine=pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    time=int(datetime.datetime.now().hour)
    if time>=0 and time<12 :
        speak("Good Morning sir.")
    elif time>=12 and time<=18 :
        speak("Good Afternoon sir.")
    else:
        speak("Good Evening sir.")
    speak("I am Jarvis. How Can I Help you . ")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query} \n")

    except Exception as e:
        print("Sorry i can't catch Your last word, Would you please repeat.")
        return "None"
    return query

if __name__=="__main__":
    wish()
    while True :
            query=takecommand().lower()
            if "wikipedia" in query:
                speak("Searching on Wikipedia...")
                query = query.replace('wikipedia...')
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)
                

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                    

            elif 'open google' in query:
                webbrowser.open("google.com")
                
            elif 'who creates you' in query:
                speak("Tejas created me")
                
        #elif "advice" in query:
            #speak("Here's an advice for you, mam")
            #advice = get_random_advice()
            #speak(advice)
           # speak("for your convinience, I am printing it on the screen")
           # print(advice)

            elif 'the time' in query:
                strTime = datetime.datetime.now().strTime("%H:%M:%S")
                speak("The time is {strTime}")
                
            elif ' how are you' in query:
                speak("I am fine")
            
            elif 'logout' in query:
                speak("Thank you")
                exit()

