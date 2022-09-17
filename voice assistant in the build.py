import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os 
import pywhatkit
import time
import sys
import requests
import wolframalpha
import json


# from ecapture import ecapture as ec  




engine = pyttsx3.init('sapi5')   #microsoft speech api-inbuilt voice use of windows
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)






def speak(audio):
    engine.say(audio);
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")

    speak("I am Ashkid, your companion Robo!")

    

def takeCommand(): #speech intake from microphone and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening.....")
        r.phrase_threshold = 0.3
        r.non_speaking_duration = 0.6
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in' )
        print(f"User said: {query}\n ")

    except Exception as e:
        # print(e) if we keep this it will display the error in detail

        #print("Could you say that again please....")
        return"None"

    return query


if __name__ == "__main__":
    print("Initializing Ashkid")
    
    
    WAKE = "hi donkey"
    while True:
        
        query = takeCommand().lower()  
            
        if query.count(WAKE)>0:
            wishMe()
            speak("How may I help you today")
            query = takeCommand().lower()


            if 'wikipedia' in query:
                speak('Searching for wikipedia ...')
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, 2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            #elif (query == "get " or query =="info"):
                #speak("On it")




            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.in")

            elif'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'play' in query:
                speak('Playing on youtube')
                query = query.replace("youtube","")
                results = query.replace('play','')
                speak(results)
                pywhatkit.playonyt(results)
            
            elif 'the time' in query or 'time' in query:
                strTime =  datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")

            elif "open visual studio" in query or "open vs code" in query:
                speak("Opening Visual Studio")
                vspath = "C:\\Users\\diksh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(vspath)

            
            elif "today's date" in query:
                strDate = datetime.datetime.today().strftime("%b-%d-%Y")
                strDay = datetime.datetime.today().strftime("%A")
                speak(f" Today's date is {strDate} and its a {strDay}")

            elif 'search' in query:
                url = 'https://www.google.co.in/search?q='
                search_url = url + query[6:]
                webbrowser.open(search_url)

            
            elif 'open gmail' in query:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail is open now")

            elif 'i have a question' in query or 'ask' in query:
                speak("I can answer computational and geographical questions for you")    
                question = takeCommand()
                app_id = "45LV6Q-HQYTWQR7GW"
                client = wolframalpha.Client('45LV6Q-HQYTWQR7GW')
                res = client.query(question)
                answer = next(res.results).text
                speak(answer)
                print(answer)

            elif 'weather' in query:
                api_key = "2bbe8e0344507f77753e3e2f4d8421b1"
                base_url = "https://api.openweathermap.org/data/2.5/weather?"
                speak("What is the name of the city?")
                city_name = takeCommand()
                complete_url = base_url+ "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x= response.json()
                if x["cod"]!="404":
                    y= x["main"]
                    current_temperature = y["temp"]
                    current_humidity = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" The weather in" + (city_name)+ " is")
                    speak("The temperature is: "+ str((current_temperature-273.1)) + " Celcius" +"\nThe humidity is: " + str(current_humidity)+"percent" + "\nDescription of weather: " + str(weather_description))
                    print("The weather in " + (city_name)+ " is:")
                    print("The temperature is: "+ str((current_temperature-273.1))+ " Celcius" +"\nThe humidity is: " + str(current_humidity)+"percent"+ "\nDescription of weather:" + str(weather_description))

            elif "great job" in query or "good job" in query:
                speak("Thank you so much Diksha, happy to help")
                print("Thank you so much Diksha, happy to help")

            else:
                    speak("sorry i didnt hear you, could you start again")
                    print("sorry i didnt hear you, could you start again")

                    query = takeCommand().lower()

                    if 'wikipedia' in query:
                        speak('Searching for wikipedia ...')
                        query = query.replace("wikipedia","")
                        results = wikipedia.summary(query, 2)
                        speak("According to Wikipedia")
                        print(results)
                        speak(results)


                    elif 'open youtube' in query:
                        webbrowser.open("youtube.com")

                    elif 'open google' in query:
                        webbrowser.open("google.in")

                    elif'open stack overflow' in query:
                        webbrowser.open("stackoverflow.com")

                    elif 'play' in query:
                        speak('Playing on youtube')
                        query = query.replace("youtube","")
                        results = query.replace('play','')
                        speak(results)
                        pywhatkit.playonyt(results)
                    
                    elif 'the time' in query or 'time' in query:
                        strTime =  datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"The time is {strTime}")

                    elif "open visual studio" in query or "open vs code" in query:
                        speak("Opening Visual Studio")
                        vspath = "C:\\Users\\diksh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(vspath)

                    
                    elif "today's date" in query:
                        strDate = datetime.datetime.today().strftime("%b-%d-%Y")
                        strDay = datetime.datetime.today().strftime("%A")
                        speak(f" Today's date is {strDate} and its a {strDay}")

                    elif 'search' in query:
                        url = 'https://www.google.co.in/search?q='
                        search_url = url + query[6:]
                        webbrowser.open(search_url)
    
                    
                    elif 'open gmail' in query:
                        webbrowser.open_new_tab("gmail.com")
                        speak("Google Mail is open now")

                    elif 'i have a question' in query or 'ask' in query:
                        speak("I can answer computational and geographical questions for you")
                        question = takeCommand()
                        app_id = "45LV6Q-HQYTWQR7GW"
                        client = wolframalpha.Client('45LV6Q-HQYTWQR7GW')
                        res = client.query(question)
                        answer = next(res.results).text
                        speak(answer)
                        print(answer)

                    elif 'weather' in query:
                        api_key = "2bbe8e0344507f77753e3e2f4d8421b1"
                        base_url = "https://api.openweathermap.org/data/2.5/weather?"
                        speak("What is the name of the city?")
                        city_name = takeCommand()
                        complete_url = base_url+ "appid=" + api_key + "&q=" + city_name
                        response = requests.get(complete_url)
                        x= response.json()
                        if x["cod"]!="404":
                            y= x["main"]
                            current_temperature = y["temp"]
                            current_humidity = y["humidity"]
                            z = x["weather"]
                            weather_description = z[0]["description"]
                            speak(" The weather in" + (city_name)+ " is")
                            speak("The temperature is: "+ str((current_temperature-273.1)) + " Celcius" +"\nThe humidity is: " + str(current_humidity)+"percent" + "\nDescription of weather: " + str(weather_description))
                            print("The weather in " + (city_name)+ " is:")
                            print("The temperature is: "+ str((current_temperature-273.1))+ " Celcius" +"\nThe humidity is: " + str(current_humidity)+"percent"+ "\nDescription of weather:" + str(weather_description))

                    elif "great job" in query or "good job" in query:
                        speak("Thank you so much Diksha, happy to help")
                        print("Thank you so much Diksha, happy to help")
                    else:

                        print("The command was suspended, activate again")  
                        speak("The command was suspended, activate again")      


                



        

            

        









        









       #i need to focus on something also spotify
       #play something else
       #u need to create your own music directory for this
       #maybe something about tv shows
       #a little bit of personalised serial content
       # add a few more apps to opem
       #add jokes or  puns
       #try adding games
       #trivia
       #add google calender






        


        
        




