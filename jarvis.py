
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia as wp
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes
engine=pyttsx3.init()
 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("This is jarvis AI Assistant")  
def time():
    speak("the current time is")
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
def date():
    speak("The current date is")
    year=int(datetime.datetime.now().year)
    month=datetime.datetime.now().month
     
    day=datetime.datetime.now().day
    speak(year)
    speak(month)
    speak(day)
def joke():
    speak(pyjokes.get_joke())
def screenshot():
    img=pyautogui.screenshot()
    img.save("image.jpg")
def cpu():
    usage=str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery=psutil.sensors_battery();
    speak("Battery is at")
    speak(battery.percent)
    
    
def greet():
    speak("welcome back ")
    
     
    hour=datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon!")
    elif hour>=18 and hour<24:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("Jarvis assitant is at your service How can i help you")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as src:
        print("listening....")
        r.adjust_for_ambient_noise(src, duration=5)
        r.pause_threshold=1
        print("start")
        audio=r.listen(src)
        print("end")
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("say that again")
        return "None"
    return query
#greet()
#speak(takeCommand()) 
if __name__=='__main__':
    #greet()
    while True:
        query=takeCommand().lower()
        print("ins")
        print(query)
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            
            print("Searching......")
            query=query.replace("wikipedia","")
            summary=wp.summary(query,sentences=2)
            print(summary)
            speak(summary)
       
        elif "search in chrome" in query:
            speak("what u want to search")
            path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search=takeCommand().lower()
            wb.get(path).open_new_tab(search+".com") 
        elif  "logout" in query:
            os.system("shutdown -l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir="D:\\Music"
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif "remember that" in query:
            speak("what should i remember")
            data=takeCommand()
            speak("you said me to remember "+data)
            remember=open("data.txt",'w')
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember=open("data.txt",'r')
            speak("you said me to remember"+remember.read())
        elif "take screenshot" in query:
            speak("taking screenshot")
            screenshot()
        elif "cpu" in query:
            cpu()
        elif "tell me a joke" in query:
            joke()
        elif "offline" in query:
            print("here")
            break
        
