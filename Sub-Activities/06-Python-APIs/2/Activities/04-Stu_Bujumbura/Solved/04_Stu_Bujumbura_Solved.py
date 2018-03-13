# Dependencies
import requests as req
import apikeys

# Save config information
url = "http://api.openweathermap.org/data/2.5/weather"

params = {'appid': apikeys.OWM_API_KEY,
          'q': 'Bujumbura',
          'units': 'metric'}

# Get weather data
weather_response = req.get(url, params=params)
weather_json = weather_response.json()

# Get temperature from JSON response
temperature = weather_json["main"]["temp"]

# Report temperature
print("The temperature in Bujumbura is " + str(temperature) + ".")
