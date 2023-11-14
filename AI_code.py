# Import the pyttsx3 library for text-to-speech
import pyttsx3  # To install --> pip install pyttsx3

# Import the speech_recognition library for speech recognition
import speech_recognition as sr  # Also used Alising ,# To install --> pip install SpeechRecognition

# Import the datetime module for working with dates and times
import datetime  # To install --> pip install datetime

# Import the wikipedia library for fetching information from Wikipedia
import wikipedia  # To install --> pip install wikipedia

# Import the webbrowser module for opening web pages
import webbrowser  # To install --> pip install webbrowser

# Import the os module for interacting with the operating system
import os  # To install --> pip install os

# Import the requests module for sending HTTP requests
import requests  # To install --> pip install requests

# Import the BeautifulSoup class from the bs4 module for web scraping
from bs4 import BeautifulSoup  # To install --> pip install Beautifulsoap


# Initialize the text-to-speech engine using pyttsx3 with the "sapi5" speech API
engine = pyttsx3.init("sapi5")

# Get the list of available voices from the engine
voices = engine.getProperty("voices")

# Set the voice of the engine to the first voice in the list
engine.setProperty("voice", voices[0].id)


# Define a function named 'speak' that takes an 'audio' parameter
def speak(audio):
    # Use the 'say' method of the 'engine' object to speak the provided 'audio'
    engine.say(audio)

    # Use the 'runAndWait' method of the 'engine' object to ensure that the speech is executed immediately
    engine.runAndWait()


# Define a function named 'wishMe'
def wishMe():
    # Get the current hour from the system clock
    hour = int(datetime.datetime.now().hour)

    # Check the time of the day and greet the user accordingly
    if hour >= 0 and hour < 12:
        # If it's morning (hour is between 0 and 12), speak "Good Morning!"
        speak("Good Morning!")

    elif (
        hour >= 12 and hour < 18
    ):  # 13 means its 1:00 pm in 24-hrs format and goes upto 24 that means 12:00am
        # If it's afternoon (hour is between 12 and 18), speak "Good Afternoon!"
        speak("Good Afternoon!")

    else:
        # If it's evening (hour is 18 or greater), speak "Good Evening!"
        speak("Good Evening!")

    # Speak a general introduction for the voice assistant
    speak("I am a voice assistant. Please tell me how may I help you")


def set_reminder(reminder_text):
    try:
        with open("reminders.txt", "a") as file:
            file.write(f"{datetime.datetime.now()}: {reminder_text}\n")
        speak("Reminder set successfully.")
    except Exception as e:
        speak(f"Error setting reminder: {e}")


def get_weather(place):
    # Construct a search query for the weather in the specified place

    search = f"weather in {place}"
    # Construct the URL for a Google search using the search query

    url = f"https://www.google.com/search?&q={search}"
    # Send an HTTP GET request to the specified URL and store the response in 'r'

    r = requests.get(url)
    # Use BeautifulSoup to parse the HTML content of the response

    soup = BeautifulSoup(r.text, "html.parser")
    # Find the div element with the class "BNeawe" in the parsed HTML

    update = soup.find("div", class_="BNeawe").text
    # Construct a string containing the weather information for the specified place

    weather_info = f"{search} now is {update}"
    # Speak the weather information (assuming there's a function named 'speak' that handles this)

    speak(weather_info)
    # Speak the weather information

    return weather_info
    # Return the constructed weather information


# Define a function named 'takeCommand'
def takeCommand():
    # It takes microphone input from the user and returns string output

    # Create a Recognizer object from the speech_recognition module
    r = sr.Recognizer()

    # Use a microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Set the pause threshold to 0.8 seconds
        r.pause_threshold = 0.8  # It is default value. we can comment it

        try:
            # Listen for audio input from the user with a timeout of 5 seconds
            audio = r.listen(source, timeout=5)

        except sr.WaitTimeoutError:
            # If no command is received within the timeout, print a message and return "stop_listening"
            print("Listening timed out. No command received.")
            return "stop_listening"

    try:
        print("Recognizing...")

        # Use Google's Speech Recognition to convert the audio to text, specifying the language as "en-in" (English - India)
        query = r.recognize_google(audio, language="en-in")

        # Print the recognized query in lowercase
        print(f"User said: {query.lower()}\n")

    except sr.UnknownValueError:
        # If the speech recognition couldn't understand the audio, print a message and return "None"
        print("Speech Recognition could not understand audio.")
        return "None"

    except sr.RequestError as e:
        # If there is an error in requesting results from Google Speech Recognition service, print an error message and return "None"
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"

    except Exception as e:
        # If an unexpected error occurs, print an error message and return "None"
        print(f"An unexpected error occurred: {e}")
        return "None"

    # Return the recognized query in lowercase
    return query.lower()


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()
        # Check if the user's query contains the word "wikipedia" in a case-insensitive manner
        if "wikipedia" in query.lower():
            # If the condition is true, execute the following block of code

            # Speak a message indicating that the virtual assistant is searching Wikipedia
            speak("Searching Wikipedia...")

            # Modify the query to remove the word "wikipedia" for more accurate search results
            query = query.lower().replace("wikipedia", "")

            # Use the Wikipedia module to fetch a summary of the query (up to 2 sentences)
            results = wikipedia.summary(query.lower(), sentences=2)

            # Speak a message indicating that the information is from Wikipedia
            speak("According to Wikipedia")

            # Print the Wikipedia summary to the console
            print(results)

            # Speak the Wikipedia summary
            speak(results)

        # Check if the user's query contains the phrase "who made you" in a case-insensitive manner
        elif "who made you" in query.lower():
            # If the condition is true, execute the following block of code
            speak("Iam voice assistant made by Syed Jawad")  #

        # Check if the user's query contains the phrase "open github" in a case-insensitive manner
        elif "open github" in query.lower():
            # If the condition is true, execute the following block of code
            webbrowser.open("https://github.com")
            # Open the specified URL in the default web browser

        # Check if the user's query contains the phrase "what color is your Bugatti" in a case-insensitive manner
        elif "what color is your Bugatti" in query.lower():
            # If the condition is true, execute the following block of code

            # Use the 'speak' function to respond, indicating that the virtual assistant doesn't have a physical entity, as it's a virtual assistant
            speak("I don't have any physical entity, since I am a virtual assistant")

            # Exit the loop or stop further execution (assuming this code is within a loop)
            break

        # Check if the user's query contains the phrase "open youtube" in a case-insensitive manner
        elif "open youtube" in query.lower():
            # If the condition is true, execute the following block of code

            webbrowser.open("youtube.com")
            # This will simply open google webpage if open google in query.lower()

        elif "open google" in query.lower():
            # ''' Same explaination as above '''
            webbrowser.open("google.com")

        elif "open linkedin" in query.lower():
            # ''' Same explaination as above '''

            webbrowser.open("linkedin.com")

        # It will play music from files

        # This will open vs code from local
        elif (
            "open vs code" in query.lower() or "vs code" in query.lower()
        ):  # if vs code in query.lower() it will start
            codePath = (
                "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            )
            os.startfile(codePath)

        elif query.lower() == "exit":
            print("Abourting")
            break
        # this sets reminder in txt file with timestamp
        elif "set reminder" in query.lower():
            reminder_text = query.lower().split("set reminder")[1].strip()
            set_reminder(reminder_text)

        # In this , the Voice assistant give temperature which city we want of.
        elif "what's the weather" in query.lower():
            speak("Sure, please tell me the city name.")
            city_name = takeCommand()

            if city_name:
                weather_result = get_weather(city_name)
                print(weather_result)
            else:
                pass

        # Check if the user's query contains the phrase "play music" in a case-insensitive manner
        elif "play music" in query.lower():
            # If the condition is true, execute the following block of code

            # Define the directory path where the music files are stored
            music_dir = "C:\\Users\\DELL\\Desktop\\ai\\OIBSIP\\music"

            # List all the files (songs) in the specified music directory
            songs = os.listdir(music_dir)

            # Print the list of songs to the console
            print(songs)

            # Use the 'os' module to start playing the first song in the list
            os.startfile(os.path.join(music_dir, songs[0]))
            # We can also use the code accordingly in the case of music, here in my case, i have only 1 song.

            """
           Note: The above code is a sample of Voice assistant. It might look lenghty code
           but isn't ,read and apply the code. Tried to explain each and every line.
           Thankyou,Oasis infobye for this Opportunity.Completed TASK1.
           """
