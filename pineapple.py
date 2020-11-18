import pyttsx3
import speech_recognition as sr
import sys, time, os, random
import wikipedia
from datetime import datetime
import webbrowser
import urllib.request
import urllib.parse
import re

engine = pyttsx3.init()

def speak(audio):
    print('PINEAPPLE: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def Command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.  .  .")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-in')
        print('You: ' + command + '\n')

    except sr.UnknownValueError:
        speak('Sorry Jaydey, Pineapple Did Not Get That!')
        return Command()

    return command

def startCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        startcommand = r.recognize_google(audio, language='en-in')
        print('User: ' + startcommand + '\n')

    except sr.UnknownValueError:
        return startCommand()

    return startcommand


def AllCode():
    def MainCommands():
        speak("Heya Jaydey! What can i do for you?")
        while True:
            command = Command();
            command = command.lower()

            if 'start CMD' in command:
                speak("Pineapple is on it!")
                os.startfile("cmd.exe")
                speak("Pineapple has done his job!")
                startCode()

            if 'play music' in command:
                speak("Pineapple is on it!")
                webbrowser.open("https://www.youtube.com/watch?v=0HWUZm1uibM&list=PLTAc2xEtu57JB-IdXPC5jSWvyobA8Dzbo&index=2&t=0s")
                speak("Pineapple has done his job!")
                startCode()

            if 'close' in command:
                speak("Goodbye Jaydey!")
                startCode()

            if 'stop music' in command:
                speak('Pineapple got this!')
                os.system("taskkill /im chrome.exe /f")
                speak("Pineapple is successfull!")
                startCode()

            if 'exit' in command:
                speak('Okay')
                sys.exit()

            if 'who created you' in command:
                speak(r"a idiot with one's and zero's instead of braincells")
                startCode()

            if 'start minecraft' in command:
                speak('Pineapple agrees with this decision!')
                os.startfile("C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe")
                speak('Done, have fun Jaydey!')
                startCode()

            if 'start atom' in command:
                speak('Okay Jaydey. pineapple like, so got this!')
                os.startfile(r"C:\Users\JKeme\AppData\Local\atom\atom.exe")
                speak("i told you, i so got that!")
                startCode()

            if 'good job pineapple' in command:
                speak('thanks, i love you too!')
                startCode()

            if 'how are you' in command:
                speak("pineapple is fine, thanks!")
                startCode()

            if 'never mind' in command:
                speak("oh, okay!")
                startCode()

            if 'what do we call this' in command:
                speak('a disapointment!')
                startCode()

            if 'who am i' in command:
                speak('a disapointment!')
                startCode()

            if 'what time is it' in command:
                timenow= datetime.now()
                current_time = timenow.strftime("%H:%M:%S")
                speak("the current time is, " + current_time)
                startCode()

            def startCodeMusic():
                while True:
                    startcommandmusic = startCommand();
                    startcommandmusic = startcommandmusic.lower()

                    while True:
                        if 'pineapple' in startcommand:
                            MainCommands()
                        else:
                            startCodeMusic()

            def songSelect():

                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    r.pause_threshold =  1
                    audio = r.listen(source)
                try:
                    musiccommand = r.recognize_google(audio, language='en-in')
                    musicchoice = musiccommand
                    print(musicchoice)

                    query_string = urllib.parse.urlencode({"search_query" : musiccommand})
                    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                    webbrowser.open(r"http://www.youtube.com/watch?v=" + search_results[0])
                    AllCode()

                except sr.UnknownValueError:
                    return startCommand()

                    return startcommand

            if 'play a song' in command:
                songSelect()

            if 'stop chrome' in command:
                speak('Okay!')
                os.system("taskkill /im chrome.exe /f")
                speak("Pineapple is successfull!")
                startCode()

            if 'open Nextflix' in command:
                speak('Got it!')
                webbrowser.open('http://www.netflix.com/')

            if 'open discord' in command:
                speak('got it!')
                os.startfile(r'C:\Users\JKeme\AppData\Local\Discord\app-0.0.306\Discord.exe')
                startCode()

            if 'shut down laptop' in command:
                speak('okay then!')
                os.system("shutdown /s /t 1")

            def openWebsite():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Listening...")
                    r.pause_threshold =  1
                    audio = r.listen(source)
                try:
                    musiccommand = r.recognize_google(audio, language='en-in')
                    musicchoice = musiccommand
                    print(musicchoice)

                    webbrowser.open('https://www.' + musicchoice + '.com')
                    speak('done.')
                    startCode()

                except sr.UnknownValueError:
                    return openWebsite()

            if 'open a website' in command:
                speak('what website would you like to open?')
                openWebsite()

            if 'who is your girlfriend' in command:
                speak('pumpkin!')
                startCode()

            if 'marry me' in command:
                speak('Maybe, HEY PUMPKIN CAN I MARRY HIM?!')
                startCode()

    def startCode():
        while True:
            startcommand = startCommand();
            startcommand = startcommand.lower()

            while True:
                if 'pineapple' in startcommand:
                    MainCommands()
                else:
                    startCode()

    startCode()

AllCode()
