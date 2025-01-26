import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import pywhatkit
import os
import pyautogui
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Dict
import datetime
import requests
import pypdf
from googletrans import Translator
from gtts import gTTS
from bs4 import BeautifulSoup
import playsound
import psutil
import speedtest
import operator
from PyQt5 import QtWidgets , QtCore , QtGui
from PyQt5.QtCore import QTimer , QTime , QDate , Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisUI import Ui_MainWindow
import sys
import time
import turtle

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('rate',150)
print(voices)
Assistant.setProperty('voice',voices[1].id)

#speak function
def Speak(audio):
    print(" ")
    Assistant.say(audio)
    print(f":{audio}")
    print(" ")
    Assistant.runAndWait()
    
#takecommand function
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)
        try:
            print("Recognising.......")
            query = command.recognize_google(audio,language= 'en-in')
            print(f"you said : {query}")
            
        except Exception as Error:
            return "none"
        
        return query.lower()
 

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExe()

    def TaskExe(self):

       # Speak("Hello I am Jarvis sir")
        while True:
            query = takecommand()        
                
            if 'hello' in query:
                Speak("Hello sir,I am Akira.")
                Speak("Your personal ai assistant")
                Speak("How may I help You")
                
            elif 'How are you' in query:
                Speak("I am Fine Sir!")
                Speak("What About you Sir?")
                
            elif 'you need a break' in query:
                Speak("Ok sir , you can call me anytime !")
                break
            
            elif 'youtube search' in query:
                Speak("Ok sir , This is what i found for your serach")
                query = query.replace("akira","")
                query = query.replace("youtube search","")
                web = "https://www.youtube.com/results?search_query=" + query
                webbrowser.open(web)
                Speak("Done sir")
                
            elif 'google search' in query:
                Speak("This is what i found for your search sir")
                query = query.replace("akira","")
                query = query.replace("google search","")
                pywhatkit.search(query)
                Speak("Done sir")
                
            elif 'website' in query:
                Speak("Ok sir,Launching...")
                query = query.replace("akira","")
                query = query.replace("website","")
                query = query.replace(" ","")
                web1 = query.replace("open","")
                web2 = 'https://www.' + web1 + '.com'
                webbrowser.open(web2)
                Speak("Launched!")
                
            elif 'music' in query:
                Music()
                
            elif 'wikipedia' in query:
                Speak("Searching wikipedia.....")
                query = query.replace("akira","")
                query = query.replace("wikipedia","")
                wiki = wikipedia.summary(query,2)
                Speak(f"According to wikipedia : {wiki}")
                
            elif 'whatsapp' in query:
                whatsapp() 
                
            elif 'screenshot' in query:

                kk =  pyautogui.screenshot()
                kk.save('c:\\')
            
            elif 'open facebook' in query:
                Openapps()
                
            elif 'open instagram' in query:
                Openapps()
                
            elif 'open map' in query:
                Openapps()
                
            elif 'open chrome' in query:
                Openapps()
                
            elif 'close chrome' in query:
                closeapps()
                
            elif 'close youtube' in query:
                closeapps()
                
            elif 'close instagram' in query:
                closeapps()
                
            elif 'pause' in query:
                keyboard.press('space bar')
                
            elif 'restart' in query:
                keyboard.press('0')
                
            elif 'mute' in query:
                keyboard.press('1')
                
            elif 'skip' in query:
                keyboard.press('L')
                
            elif 'back' in query:
                keyboard.press('J')

            elif 'play' in query or 'can you play' in query or 'please play' in query:
                Speak("Ok! here you go!!")
                query = query.replace("play", "")
                query = query.replace("could you play", "")
                query = query.replace("please play", "")
                webbrowser.open(f'https://open.spotify.com/search/{query}')
                time.sleep(19)
                pyautogui.click(x=1055, y=617)
                print('Enjoy!' + turtle.reset())
                Speak("Enjoy Sir!")

            elif 'full screen' in query:
                keyboard.press('f')  
                
            if 'close this tab' in query:
                keyboard.press_and_release('ctrl + N')

            elif 'open new tab' in query:
                keyboard.press_and_release('ctrl + t')

            elif 'open new window' in query:
                keyboard.press_and_release('ctrl + n')

            elif 'history' in query:
                keyboard.press_and_release('ctrl + h')

            elif 'download' in query:
                keyboard.press_and_release('ctrl + d')

            elif 'chrome Automation' in query:
                chromeAuto()

            elif 'youtube Automation' in query:
                YoutubeAuto()

            elif 'joke' in query:
                get = pyjokes.get_joke()
                Speak(get)

            elif 'repeat my words' in query:
                Speak('speak sir!')
                jj = takecommand()
                Speak(f'You said: {jj}')
                
            elif 'my location' in query:
                Speak('Ok sir, wait a minute!')
                webbrowser.open('https://www.google.com/maps/place/Gadag-Betigeri,+Karnataka/@15.4290078,75.5923251,13z/data=!3m1!4b1!4m6!3m5!1s0x3bb8f96dcd4793e9:0x9c3825dd10248648!8m2!3d15.4362732!4d75.6351476!16s%2Fg%2F12m8zfpcx?entry=ttu')
                
            elif 'dictionary' in query:
                Dict()   
                
            elif 'alarm' in query:
                Speak("Enter the time !")
                time = input(": Enter the Time Sir:")
                
                while True:
                    Time_Ac = datetime.datetime.now()
                    now = Time_Ac.strftime("%H:%M:%S")
                    
                    if now == time:
                        Speak("Time To Wake Up Sir!")
                        playsound.playsound(r"C:\Users\vinut\OneDrive\Documents\advanced gui\Design\Be Notorious BGM - Bheeshma Parvam ! Malayalam.mp3")
                        Speak("Alarm Closed")
                        
                    elif now>time:
                        break
                
            elif 'temperature' in query:
                Temp()
                
            elif 'read pdf' in query:
                Reader()
                
            elif 'speed test' in query:
                SpeedTest()
                
            #elif 'translator' in query:
                #Trans()
            
            elif 'remeber that' in query:
                remeberMsg = query.replace("remeber that","")
                remeberMsg = remeberMsg.replace("akira","")
                Speak("You Tell Me to Remind You that :"+remeberMsg)
                remeber = open('data.txt','w')
                remeber.write(remeberMsg)
                remeber.close()
                
            elif 'what do you remeber' in query:
                remeber = open('data.txt','r')
                Speak("You Tell Me that"+ remeber.read())
            
            elif 'how much power left' in query or 'how much power we have' in query or 'battery' in query:
                battery()
                   
                    
            elif 'google search' in query:
                import wikipedia as googleScrap
                query = query.replace("akira","")
                query = query.replace("googlesearch","")
                query = query.replace("google","")
                Speak("This is what i found on the Web!")
                pywhatkit.search(query)
                
                try:
                    result = googleScrap.summary(query,2)
                    Speak(result)
                except:
                    Speak("No callable data")

            elif 'Do some calculations' in query or 'can you calculate' in query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    Speak("Say what you want to calculate , example : 3 plus 3")
                    print("Listening.....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)

                    def get_operator_fn(op):
                        return {
                            '+' : operator.add,
                            '-' : operator.sub,
                            'x' : operator.mul,
                            'divided' : operator.__truediv__,
                        }[op]
                    

                    def eval_binary_expr(op1 , oper , op2):
                        op1 , op2 = int(op1),int(op2)
                        return get_operator_fn(oper)(op1,op2)
                    Speak("Your result is :")
                    Speak(eval_binary_expr(*(my_string.split())))
            
            elif 'volume up' in query:
                pyautogui.press("volumeup")

            elif 'volume down' in query:
                pyautogui.press("volumedown")

            elif 'volume mute' in query or 'mute' in query:
                pyautogui.press("volumemute")

            elif 'bye' in query:
                Speak("Ok sir , bye")
                break

    #function for music
        def Music():
            Speak("tell me the name of the song!")
            musicname = takecommand()
        
            if 'akeli' in musicname:
                os.startfile('c:\\Songs\\akeli.mp3')
            elif 'blanko' in musicname:
                os.startfile('c:\\Songs\\blanko.mp3')
            else :
                pywhatkit.playonyt(musicname)
            Speak("Your song has been started!,Enjoy sir!")
    
    #function for speedtest  
        def SpeedTest():    
            Speak("Checking speed....")
            speed = speedtest.Speedtest()
            downloading = speed.download()
            correctDown = int(downloading/800000)
            uploading = speed.upload()
            correctUpload = int(uploading/800000)
            
            if 'uploading' in query:
                Speak(f"The Uploading speed is {correctUpload} mbps")    
            
            elif 'downloading' in query:
                Speak(f"The downloading speed is {correctDown} mbps ")    
                
            else:
                Speak(f"The Downloading speed is {correctDown} and The uploading Speed is {correctUpload}")
    
    #function for whatsapp          
        def whatsapp():
                Speak("Tell me the name of the person!")
                name = takecommand()
                
                if 'karan' in name:
                    Speak("Tell Me the message!")
                    msg = takecommand()
                    Speak("Tell me the time sir !")
                    Speak("Time in hour!")
                    hour = int(takecommand())
                    Speak("Time in minute!")
                    min = int(takecommand())
                    pywhatkit.sendwhatsmsg("+919148595747",msg,hour,min,20)
                    Speak("Ok sir ,Sending whatsapp message !")
                    
                elif 'ajay' in name:
                    Speak("Tell Me the message!")
                    msg = takecommand()
                    Speak("Tell me the time sir !")
                    Speak("Time in hour!")
                    hour = int(takecommand())
                    Speak("Time in minute!")
                    min = int(takecommand())
                    pywhatkit.sendwhatsmsg("+918867937327",msg,hour,min,20)
                    Speak("Ok sir ,Sending whatsapp message !")
                    
                elif 'anil' in name:
                    Speak("Tell Me the message!")
                    msg = takecommand()
                    Speak("Tell me the time sir !")
                    Speak("Time in hour!")
                    hour = int(takecommand())
                    Speak("Time in minute!")
                    min = int(takecommand())
                    pywhatkit.sendwhatsmsg("+919148595747",msg,hour,min,20)
                    Speak("Ok sir ,Sending whatsapp message !")
    
    
    #function for reading pdf
        def Reader():
            Speak("Tell me the name of the book")
            
            name = takecommand()
            
            if 'india' in name:
                os.startfile(r'C:\Users\vinutmaradur\Documents\VI sem\python\unit-1')
                book = open(r'C:\Users\vinutmaradur\Documents\VI sem\python\unit-1','rb')
                pdfreader = pypdf.PdfFileReader(book)
                pages = pdfreader.getNumPages()
                Speak(f"Number of Pages in this books are{pages}")
                Speak("From Which page I have to start reading ?")
                numPage = int(input("Enter the page number:"))
                page = pdfreader.getpage(numPage)
                text = page.extractText()
                Speak("In which language , I have to read ?")
                lang = takecommand()
                
                if 'hindi' in lang:
                    trans1 = Translator()
                    textHin = trans1.translate(text,'hi') 
                    textm = textHin.text
                    speech = gTTS(text = textm)
                    try:
                        speech.save('book.mp3')
                        playsound('book.mp3')
                    except:
                        playsound('book')
                else:
                    Speak(text)
            
            elif 'europe' in name:
                os.startfile('')
                book = open('','rb')
                pdfreader = pypdf.PdfFileReader(book)
                pages = pdfreader.getNumPages()
                Speak(f"Number of Pages in this books are{pages}")
                Speak("From Which page I have to start reading ?")
                numPage = int(input("Enter the page number:"))
                page = pdfreader.getpage(numPage)
                text = page.extractText()
                Speak("In which language , I have to read ?")
                lang = takecommand()
                        
                if 'hindi' in lang:
                    trans1 = Translator()
                    textHin = trans1.translate(text,'hi') 
                    textm = textHin.text
                    speech = gTTS(text = textm)
                    try:
                        speech.save('book.mp3')
                        playsound('book.mp3')
                    except:
                        playsound('book')
                else:
                    Speak(text)  
                
    #function for opening apps                  
        def Openapps():
            Speak("Ok sir , wait a second!")
            
            if 'code' in query:
                os.startfile("C:\Program Files\Microsoft VS Code\Code.exe")
            elif 'telegram' in query:
                os.startfile("C:\Program Files\Microsoft\Edge\Application\msedge.exe")
            elif 'whatsapp' in query:
                webbrowser.open('https://www.whatsapp.com/')
            elif 'chrome' in query:
                webbrowser.open('https://www.chrome.com/')
            elif 'facebook' in query:
                webbrowser.open('https://www.facebook.com/')
            elif 'instagram' in query:
                webbrowser.open('https://instagram.com/')
            elif 'maps' in query:
                webbrowser.open('https://www.google.com//maps/')
            Speak("Your command has been successfully completed")
      
    #function for closing apps    
        def closeapps():
            Speak("Ok sir,wait a second")
            if 'youtube' in query:
                os.system("TASKKILL /f /im chrome.exe")
            elif 'chrome' in query:
                os.system("TASKKILL /f /im chrome.exe")
            elif 'telegram' in query:
                os.system("TASKKILL /f /im telegram.exe")
            elif 'instagram' in query:
                os.system("TASKKILL /f /im instagram.exe")
        
    #function for youtube automation
        def YoutubeAuto():
            Speak("What's your command") 
            com = takecommand()
            
            if 'pause' in com:
                keyboard.press('space bar')
            elif 'restart' in com:
                keyboard.press('0')
            elif 'mute' in com:
                keyboard.press('1')
            elif 'skip' in com:
                keyboard.press('L')
            elif 'back' in com:
                keyboard.press('J')
            elif 'full screen' in com:
                keyboard.press('f')   
    
    #function for checking temperature
        def Temp():
            search = "temperature in karnataka"
            url = f"https://www.google.com/search?q= {search}"
            r= requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div", class_ = "BNeawe").text
            Speak(f"The temperature outside is {temperature} celsuis")
    
    #function for chrome automation
        def chromeAuto():
            Speak("Chrome Automation started")
            com = takecommand()
            
            if 'close this tab' in com:
                keyboard.press_and_release('ctrl + N')
            elif ' open new tab' in com:
                keyboard.press_and_release('ctrl + t')
            elif 'open new window' in com:
                keyboard.press_and_release('ctrl + n')
            elif 'history' in com:
                keyboard.press_and_release('ctrl + h')
            elif 'download' in com:
                keyboard.press_and_release('ctrl + d')
    
    #function for checking battery percentage
        def battery():
            battery = psutil.sensors_battery()
            percentage = battery.percent
            Speak(f"sir our system have {percentage} percent battery")
            if percentage>=75:
                Speak("we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                Speak("We should connect our system to charging point to charge our battery")
            elif percentage<=15 and percentage<=30:
                Speak("We don't have enough power to work , please connect to charging")
            elif percentage<=15:
                Speak("We have low power , please connect to charging the system will shutdown very soon")
                
        #function for taking screenshot        
        def screenshot():
            Speak('Ok Boss. what should i name that file')
            path = takecommand()
            pathname = path + '.png'
            path1 = "c:\\" + pathname
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile('C:\\')
            Speak("Here is your screenshot")
        
        #function for translating from english to hindi language    
        # def TakeHindi():
        #         command = sr.Recognizer()
        #         with sr.Microphone() as source:
        #             print("Listening.....")
        #             command.pause_threshold = 1
        #             audio = command.listen(source)
        #         try:
        #             print("Recognising.......")
        #             query = command.recognize_google(audio,language= 'hi')
        #             print(f"you said : {query}")
                
        #         except Exception as Error:
        #             return "none"
            
        #         return query.lower()
            
        # def Trans():
        #     Speak("Tell Me the line !")
        #     line = TakeHindi()
        #     translate = Translator()
        #     result = translate.translate(line)
        #     Text = result.text
        #     Speak("The translation for this line is :"+ Text)
        
        #function for searching anything in dictionary    
        def Dict():
            Speak('Activated Dictionary')
            Speak('Tell me the problem!')
            prob = self.takecommand()  
            
            if 'meaning' in prob:
                prob = prob.replace("What is","")
                prob = prob.replace("john","")
                prob = prob.replace("of","")
                prob = prob.replace("meaning of","")
                result = Dict.meaning(prob)
                Speak(f"The meaning of {prob} is {result}")
            elif 'synonyms' in prob:
                prob = prob.replace("What is","")
                prob = prob.replace("jarvis","")
                prob = prob.replace("of","")
                prob = prob.replace("synonyms of","")
                result = Dict.synonyms(prob)
                Speak(f"The synonyms of {prob} is {result}")
            elif 'antonyms' in prob:
                prob = prob.replace("What is","")
                prob = prob.replace("jarvis","")
                prob = prob.replace("of","")
                prob = prob.replace("Antonym of","")
                result = Dict.antonym(prob)
                Speak(f"The Antonym of {prob} is {result}")    
            Speak("Exited Dictionary!")
        

        while True:
            self.query = self.takecommand().lower()
            #song
            if 'song please' in self.query or 'play some song' in self.query or 'could you play some song' in self.query:
                Speak('Sir what should I play...')
                song = self.takecommand()
                webbrowser.open(f'https://open.spotify.com/search/{song}')
                time.sleep(10)
                pyautogui.click(x=1055, y=617)
                Speak('Playing' + song)
            #spotify
            # elif 'play' in self.query or 'can you play' in self.query or 'please play' in self.query:
            #     Speak("Ok! here you go!!")
            #     self.query = self.query.replace("play", "")
            #     self.query = self.query.replace("could you play", "")
            #     self.query = self.query.replace("please play", "")
            #     webbrowser.open(f'https://open.spotify.com/search/{self.query}')
            #     time.sleep(19)
            #     pyautogui.click(x=1055, y=617)
            #     print('Enjoy!' + turtle.reset())
            #     Speak("Enjoy Sir!")
         
        
         
    

startExecution = MainThread()

class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)
        self.jarvis_ui.pushButton.clicked.connect(self.startTask)
        self.jarvis_ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.jarvis_ui.movies = QtGui.QMovie("Gui ai/B.G/Black_Template.jpg")
        self.jarvis_ui.label.setMovie(self.jarvis_ui.movies)
        self.jarvis_ui.movies.start()

        self.jarvis_ui.movies_2 = QtGui.QMovie("Gui ai/B.G/Iron_Template_1.gif")
        self.jarvis_ui.label_2.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_3 = QtGui.QMovie("Gui ai/ExtraGui/initial.gif")
        self.jarvis_ui.label_3.setMovie(self.jarvis_ui.movies_3)
        self.jarvis_ui.movies_3.start()

        self.jarvis_ui.movies_4 = QtGui.QMovie("Gui ai/ExtraGui/Code_Template.gif")
        self.jarvis_ui.label_4.setMovie(self.jarvis_ui.movies_4)
        self.jarvis_ui.movies_4.start()

        self.jarvis_ui.movies_5 = QtGui.QMovie("Gui ai/ExtraGui/Hero_Template.gif")
        self.jarvis_ui.label_5.setMovie(self.jarvis_ui.movies_5)
        self.jarvis_ui.movies_5.start()

        timer = QTimer(self)
        # timer.timeout.connect(self.showTime)
        timer.start(5000)
        startExecution.start()

    # def showTime(self):
    #     current_time = QTime.currentTime()
    #     current_date = QDate.currentDate()
    #     label_time = current_time.toString('hh:mm:ss')
    #     label_date = current_date.toString(Qt.ISODate)
    #     self.ui.textBrowser.setText(label_date)
    #     self.ui.textBrowser_2.setText(label_time)

Gui_app = QApplication(sys.argv)
Gui_jarvis = Gui_Start()
Gui_jarvis.show()
exit(Gui_app.exec_())

