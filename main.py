import requests
import json
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    city = input("Enter the name of the city (or 'q' to quit):\n")

    if city == "q":  # Check if the user wants to quit
        speak("App is closing. Bye bye!")
        break

    url = f"https://api.weatherapi.com/v1/current.json?key=2299544129f94641913145500251502&q={city}"
    r = requests.get(url)


    wdic = json.loads(r.text)
    w = wdic["current"]["temp_c"]
    speak(f"The current weather in {city} is {w} degrees")
    print(w)

