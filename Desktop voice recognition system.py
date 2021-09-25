import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')                     
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice', voices[2].id)       

def speak(audio):                                  
   engine.say(audio)
   engine.runAndWait()


def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I'm Zira Sir. Please tell me how may I help you")


def takeCommand():
    r= sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening....")       
        r.pause_threshold = 1  
        audio = r.listen(source)    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
       #print(f"User said: {query}\n")
        print("User said: \n", query)

    except Exception as e:
        print("Please! Say it again")
        return "None" 
    return query





if __name__ == "__main__":
    wishme()
    while True:
        #if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open_new("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open_new("https://www.google.com")
        elif 'open facebook' in query:
            webbrowser.open_new("https://www.facebook.com")
        elif 'open instagram' in query:
            webbrowser.open_new("https://www.instagram.com")
        elif 'open twitter' in query:
            webbrowser.open_new("https://www.twitter.com")
        elif 'open stackoverflow' in query:
            webbrowser.open_new("https://www.stackover.com")

        elif 'play music' in query:
            music_dir = 'E:\\Music\\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[1]))
    
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open practical' in query:
            practicalPath = "C:\\Users\\hp\\Desktop\\Practical"
            os.startfile(practicalPath)
        elif 'email to satyam' in query:
           try:
              speak("What should I say")
              content= takeCommand()
              to= "satyamsing026.iiitp@gmail.com"
              sendEmail(to,content)
              speak("Email has been sent!")
           except Exception as e:
                print(e)
                speak("Sorry my friend, I'm not able to sent this Email")
