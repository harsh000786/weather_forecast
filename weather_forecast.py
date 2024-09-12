import requests
import json
import pyttsx3


e = pyttsx3.init()


city = input("enter the name of the city\n")


url = f"https://api.weatherapi.com/v1/current.json?key=33216341706d4cb18b752850241209&q={city}&aqi=no"
r = requests.get(url)


wdic = json.loads(r.text)


w = wdic["current"]["temp_c"]
f = wdic["current"]["wind_kph"]
c = wdic["current"]["wind_dir"]
i = wdic["current"]["pressure_mb"]
g = wdic["current"]["heatindex_f"]
t = wdic["location"]["localtime"]
h = wdic["current"]["humidity"]

e.say(f"the current weather in {city} is {w}")
e.runAndWait()

while True:
    e.say("If you need detailed information about the region, type the details below")
    e.runAndWait()

    print("wind, pressure, heat index, local time, humidity")
    x = input("enter a key word: ")

    if x == "wind":
        e.say(f"The wind speed is {f} kilometers per hour and the wind direction is {c}.")
        e.runAndWait()
        break

    elif x == "pressure":
        e.say(f"The pressure is {i} millibars.")
        e.runAndWait()
        break

    elif x == "heat index":
        e.say(f"The heat index is {g} degrees Fahrenheit.")
        e.runAndWait()

    elif x == "local time":
        e.say(f"The local time is {t}.")
        e.runAndWait()
        break

    elif x == "humidity":
        e.say(f"The humidity level is {h}%.")
        e.runAndWait()
        break

    else:
        e.say("Not a valid command.")
        e.runAndWait()
        break
