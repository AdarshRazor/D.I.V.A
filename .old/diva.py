import pyttsx3                                  #pip install pyttsx3
import speech_recognition as sr                 #pip install speechRecognition
import datetime                                 #default
import wikipedia                                #pip install wikipedia
import webbrowser                               #default
import os                                       #default
from gtts import gTTS                           #pip install gTTS
import pygame as pg                             #pip install pygame
import certifi                                  #default
import urllib3                                  #default
import ssl                                      #default
import requests                                 #default
import time                                     #default
import urllib.parse                             #default
#from urllib.parse import urlparse              #default
from playsound import playsound                 #pip install playsound
#import validators                              #pip install validators
import smtplib                                  #default
import requests                                 #default
import tkinter                                  #default
from tkinter.filedialog import *                #default
import random as r                              #default
from requests.packages.urllib3.exceptions import InsecureRequestWarning
#import comtypes.client
#from comtypes.gen import SpeechLib
#from comtypes.client import CreateObject

root = tkinter.Tk()
#root.mainloop()
root.overrideredirect(1)
root.withdraw()
root.focus()
root.lift()



"""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
print (type(voices))
engine.setProperty('voice', voices[0].id)
"""


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
#import comtypes.client
#from comtypes.gen import SpeechLib
#from comtypes.client import CreateObject

'''
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
print (type(voices))

engine.setProperty('voice', voices[0].id)
'''
os.system("clear")
def speak(audioString):
    print("\t",audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    playsound("audio.mp3")
    #pygame.mixer.music.load("audio.wav")
    #pygame.mixer.music.play(0)
    #time.sleep(0.25)
    #os.system("mpg321 audio.wav -q")
    #os.system("mplayer -af scaletempo -speed 1.4 audio.wav")
    #os.system("ffplay -nodisp -af 'atempo=1.2' -loglevel quiet -autoexit audio.wav")
    #os.system("ffplay -af 'atempo=1.5' -loglevel quiet -t 5  audio.wav")
def play_sound(music_file, volume=1.0):
    '''
    stream music with mixer.music module in a blocking manner
    this will stream the sound from disk while playing
    '''
    # set up the mixer
    freq = 25000   # audio CD quality, basically the speed in which the audio is played
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2500    # number of samples (experiment to get best sound)
    pg.mixer.init(freq, bitsize, channels, buffer)
    # volume value 0.0 to 1.0
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        #print("Music file {} loaded!".format(music_file))
    except pg.error:
        #print("File {} not found! ({})".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play(loops=0)
    #pg.mixer.music.stop()
    while pg.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(10)
        print ("clock : ",clock)
    pg.mixer.music.play(loops=0)
    pg.mixer.music.pause()
    pg.mixer.music.stop()    
    #os.remove("audio.mp3")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! I am DIVA. How may I help you ?")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! I am DIVA. How may I help you ?")   

    else:
        speak("Good Evening! I am DIVA. How may I help you ?")  

    #speak("I am DIVA Sir. How may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail', 'password')
    server.sendmail('youremail', to, content)
    server.close()


def url_validator(url,url_2):
    new = 2
    try:
        request = requests.get(url)
        if request.status_code == 200:
            webbrowser.open(url, new=new)
    except:
        #speak("Could not find the url you were looking for, returning a google search on the same")
        print("Could not find the url %s , returning a google search on the same"%(url))        
        base_url = "http://www.google.com/?#q="
        final_url = base_url + urllib.parse.quote(url_2)
        webbrowser.open(final_url, new=new) 



def google_search(search):
    new = 2
    base_url = "http://www.google.com/?#q="
    final_url = base_url + urllib.parse.quote(search)
    webbrowser.open(final_url, new=new)

def youtube(y):
    new = 2
    base_url = "https://www.youtube.com/results?search_query="
    final_url = base_url + urllib.parse.quote(y)
    webbrowser.open(final_url, new=new)

if __name__ == "__main__":
    wishMe()
    count = 0
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            count = 0
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'search' in query:
            search = query[6:]
            count = 0
            google_search(search)

        elif 'open' in query:
            l = query.split()
            l.pop(0)
            s = ""
            x = s.join(l)
            url_2 = query[5:]
            url = "https://www.%s.com/"%(x)
            count = 0
            url_validator(url,url_2)

        elif 'youtube' in query:
            y = query[len('youtube'):]
            count = 0
            youtube(y)

        elif 'play music' in query:
            music_dir = askdirectory()
            songs = os.listdir(music_dir)
            count = 0
            print(songs,"\n\n")
            #speak ("Playing random music from the chosen folder")
            print ("Playing random music from the chosen folder")    
            os.startfile(os.path.join(music_dir, r.choice(songs)))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = askdirectory()
            count = 0
            os.startfile(codePath)

        elif 'email to saket' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "saketsavarn07@gmail.com"    
                sendEmail(to, content)
                count = 0
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")
        elif count>10:
            #speak("Exiting due to ignorance")
            print("\t\tExiting due to ignorance\n\n\n")
            exit()
        else:
            #speak("Sorry I didn't get that!")    
            print("\tSorry I didn't get that!\n")
        count += 1    
