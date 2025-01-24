from http import client
from openai import OpenAI
from setuptools import Command
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrery
import requests
from openai import OpenAI
from gtts import gTTS



#pip install pocketsphinx



recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "c3b09a472fb04f0ba2453b4a67e9dc2d"
  
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
     tts = gTTS(text)
     tts.save('hello.mp3')
    
def aiProcess(command):
    client = OpenAI (
  api_key="c3b09a472fb04f0ba2453b4a67e9dc2d",
)
  
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
   {"role":"system","content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
   {"role": "user","content": Command}
   ]
   )

completion.choices[0].message.content
  
def processCommand(c):
    if "open google" in c.lower():
       webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrery.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            
            #Parse the JSON response
            data = r.json()
        
            #Extract the articles
            articles = data.get('articles', [])
        
            #print the headlines
            for article in articles:
                speak(article['title'])
                
    else:
       #Let openAI handle the request
       output = aiProcess(c)
       speak(output)
       
                
  
if __name__== "__main__":
   speak("Initializing Jarvis....")
   while True:
    
        #Listen for wake word "Jarvis"
        #obtain audio from the microphone
  
      r = sr.Recognizer()
           
      print("recognizing...")
      try:
          with sr.Microphone() as source:
              print("Listensing...")
              audio = r.listen(source, timeout=2, phrase_time_limit=1)
          word = r.recognize_google(audio)
          if(word.lower() == "Jarvis"):        
             speak("Ya")
             #Listen for command
             with sr.Microphone() as source:
                 print("Jarves Active...")
                 audio = r.listen(source)
                 command = r.recognize_google(audio)
                 
                 processCommand(command)   
             
      except Exception as e:
        print("Error; {0}".format(e))
           

  
  
