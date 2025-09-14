###################################################################################################
# What is the current weather in a given city?
#
# Create your own API-key at home.openweathermap.org (https://home.openweathermap.org/api_keys) :
#  JSON-structure doc here: https://openweathermap.org/current
#
# Jocke C 2025
###################################################################################################
import json
import requests


API_KEY = "..."  # <- Enter your API key here
url = "https://api.openweathermap.org/data/2.5/weather"
city = input(f"Enter city: ")

# params = {"q": "Stockholm", "appid": API_KEY, "units": "metric"}
params = {"q": city, "appid": API_KEY, "units": "metric"}

r = requests.get(url, params=params)
data = r.json()

print("City:", data["name"])
print("Country:", data["sys"]["country"])
print("Temp:", data["main"]["temp"], "°C")
print("Feels like:", data["main"]["feels_like"], "°C")
print("Wind speed:", data["wind"]["speed"], "m/s")
print("Wind direction:", data["wind"]["deg"], "")
print("Weather:", data["weather"][0]["description"])
print("")

#############################################
#  Fetch and print the entire JSON structure
print("--- Whole JSON-structure ---")
print(json.dumps(data, indent=4))
