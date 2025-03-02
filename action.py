import datetime
import speak
import webbrowser
import weather
import wikipedia
import speech_recognition as sr
import os
def get_input():
    """Function to take input from either speech or text."""
    choice = input("Enter '1' for text input, '2' for voice input: ")

    if choice == '1':
        return input("Type your command: ").lower()  # Take text input
    elif choice == '2':
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio).lower()  # Convert speech to text
        except sr.UnknownValueError:
            speak.speak("Sorry, I didn't catch that.")
            return ""
    else:
        speak.speak("Invalid choice. Please enter '1' or '2'.")
        return ""

def Action(send):   
    data_btn = send.lower()

    if "what is your name" in data_btn:
        speak.speak("My name is Virtual Assistant")  
        return "My name is Virtual Assistant"

    elif "hello" in data_btn:
        speak.speak("Hey sir, how can I help you?")
        return "Hey sir, how can I help you?" 

    elif "how are you" in data_btn:
        speak.speak("I am doing great these days, sir") 
        return "I am doing great these days, sir"   

    elif "thank you" in data_btn:
        speak.speak("It's my pleasure, sir, to assist you.")
        return "It's my pleasure, sir, to assist you."

    elif "time" in data_btn or "what is the time" in data_btn:
        current_time = datetime.datetime.now().strftime("%H Hour : %M Minute")
        speak.speak(f"The time is {current_time}")
        return f"The time is {current_time}" 

    elif "shutdown" in data_btn or "quit" in data_btn:
        speak.speak("Okay sir, shutting down.")
        os.system("shutdown /s /t 5") 
        return "Okay sir, shutting down."

    elif "play music" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("Gaana.com is now ready for you. Enjoy your music!")                   
        return "Gaana.com is now ready for you. Enjoy your music!"

    elif "open google" in data_btn:
        webbrowser.open("https://google.com/")
        speak.speak("Google is open.")  
        return "Google is open."
    
    elif "open chatgpt" in data_btn:
        webbrowser.open("https://chatgpt.com/")
        speak.speak("Chatgpt is open.")  
        return "Chatgpt is open."

    elif "open youtube" in data_btn:
        webbrowser.open("https://youtube.com/")
        speak.speak("YouTube is open.") 
        return "YouTube is open."

    elif "weather" in data_btn:
        ans = weather.Weather()
        speak.speak(ans) 
        return ans

    elif "search wikipedia" in data_btn or "tell me about" in data_btn:
        try:
            query = data_btn.replace("search wikipedia", "").replace("tell me about", "").strip()
            if query:
                summary = wikipedia.summary(query, sentences=2)
                speak.speak(summary)
                return summary
            else:
                speak.speak("Please provide a topic to search on Wikipedia.")
                return "Please provide a topic to search on Wikipedia."
        except wikipedia.exceptions.DisambiguationError as e:
            speak.speak("There are multiple results. Please be more specific.")
            return "There are multiple results. Please be more specific."
        except wikipedia.exceptions.PageError:
            speak.speak("No relevant page found on Wikipedia.")
            return "No relevant page found on Wikipedia."

    elif "google" in data_btn:
        query = data_btn.replace("google", "").strip()
    
        if query:
           url = f"https://www.google.com/search?q={query}"
           webbrowser.open(url)
           return f"Searching Google for {query}..."
        else:
           return "Please mention what you want to search on Google."

    else:
        speak.speak("I'm unable to understand!")
        return "I'm unable to understand!"   

# Running the Assistant
user_input = get_input()
if user_input:
    response = Action(user_input)
    print(response)
