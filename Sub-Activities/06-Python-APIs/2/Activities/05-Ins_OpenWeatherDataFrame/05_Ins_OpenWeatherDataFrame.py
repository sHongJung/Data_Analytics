
# Dependencies
import matplotlib.pyplot as plt
import requests as req
import pandas as pd
import apikeys

# Save config information
url = "http://api.openweathermap.org/data/2.5/weather"

params = {'appid': apikeys.OWM_API_KEY,
          'q': '',
          'units': 'metric'}

weather_data = []
cities = ["Paris", "London", "Oslo", "Beijing"]

# Loop through the list of cities and perform a request for data on each
for city in cities:
    # Get weather data
    params['q'] = city
    response = req.get(url, params=params).json()
    weather_data.append(response)

print(weather_data)

# Create lists of latitudes and temperatures
lat_data = []
temp_data = []
for data in weather_data:
    lat_data.append(data['coord']['lat'])
    temp_data.append(data['main']['temp'])
# Shortcut:
# lat_data = [data['coord']['lat'] for data in weather_data]
# temp_data = [data['main']['temp'] for data in weather_data]

weather_dict = {"temp": temp_data, "lat": lat_data}
weather_data_df = pd.DataFrame(weather_dict)
print(weather_data_df.head())

# Build a scatter plot for each data type
plt.scatter(weather_data_df["lat"], weather_data_df["temp"], marker="o")

# Incorporate the other graph properties
plt.title("Temperature in World Cities")
plt.ylabel("Temperature (Celsius)")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("TemperatureInWorldCities.png")

# Show plot
plt.show()
