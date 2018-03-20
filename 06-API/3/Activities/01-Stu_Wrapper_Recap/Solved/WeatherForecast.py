# Dependencies
import requests
import json

# Weather
api_key = "c7f9f57b4779391ea1f5ae067591c971"

# Endpoint URL for five day forecast Phoenix, AZ
target_url = "http://api.openweathermap.org/data/2.5/forecast" \
    "?q=Phoenix,us&units=IMPERIAL&mode=json&APPID=" + api_key

# Print URL
print(target_url)

# Request Data
city_weather = requests.get(target_url).json()

# Display the weather with dates
for temp in city_weather["list"]:
    print("%s | %s F" % (temp["dt_txt"], temp["main"]["temp"]))
