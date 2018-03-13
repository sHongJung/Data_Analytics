# Dependencies
import json
import requests as req
import apikeys

# Save config information
url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = apikeys.OWM_API_KEY
city = 'London'

# Build query URL
query_url = url + '?appid=' + api_key + '&q=' + city

# Get weather data
weather_response = req.get(query_url)
weather_json = weather_response.json()

# Print response
print("The weather API responded with: ")
print(json.dumps(weather_json, indent=4, sort_keys=True))
print()

# Query parameters can be set using a dictionary
parameters = {'appid': apikeys.OWM_API_KEY,
              'q': 'Brussels'}

# Get weather data
weather_response = req.get(url, params=parameters)
weather_json = weather_response.json()

# Print response
print("The weather API responded with: ")
print(json.dumps(weather_json, indent=4, sort_keys=True))
print()
