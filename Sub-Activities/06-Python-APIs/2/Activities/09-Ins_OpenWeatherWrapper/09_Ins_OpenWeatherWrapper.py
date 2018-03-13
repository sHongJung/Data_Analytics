# Dependencies
import json
import openweathermapy.core as ow
import apikeys

# Create settings dictionary with information we're interested in
api_key = apikeys.OWM_API_KEY

# OpenWatherMapy makes it easy to send a request
current_weather_paris = ow.get_current("Paris", units="metric",
                                       appid=api_key)

# Print the response
print("Current weather object for Paris: ")
print(json.dumps(current_weather_paris, indent=4, sort_keys=True))

print('Type of response:', type(current_weather_paris))

name = current_weather_paris['name']
temp = current_weather_paris['main']['temp']
data = (name, temp)
print("The current weather summary for Paris is: " + str(data))

data = current_weather_paris('name', 'main.temp')
print("The current weather summary for Paris is: " + str(data))
