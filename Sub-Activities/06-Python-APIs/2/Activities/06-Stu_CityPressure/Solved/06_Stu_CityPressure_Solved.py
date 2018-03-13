
# Dependencies
import matplotlib.pyplot as plt
import requests as req
import pandas as pd
import apikeys

# Save config information
url = 'http://api.openweathermap.org/data/2.5/weather'

params = {'appid': apikeys.OWM_API_KEY,
          'q': '',
          'units': 'metric'}

weather_data = []
cities = ['London', 'Paris', 'Las Vegas', 'Stockholm', 'Sydney', 'Hong Kong']

# Loop through the list of cities and perform a request for data on each
for city in cities:
    # Get weather data
    params['q'] = city
    response = req.get(url, params=params).json()
    weather_data.append(response)

print(weather_data)

# Create lists of longitudes and atmospheric pressures
lon_data = []
pressure_data = []
for data in weather_data:
    lon_data.append(data['coord']['lon'])
    pressure_data.append(data['main']['pressure'])
# Shortcut:
# lon_data = [data['coord']['lon'] for data in weather_data]
# pressure_data = [data['main']['pressure'] for data in weather_data]

weather_dict = {'pressure': pressure_data, 'lon': lon_data}
weather_data_df = pd.DataFrame(weather_dict)
print(weather_data_df.head())

# Build a scatter plot for each data type
plt.scatter(weather_data_df['lon'], weather_data_df['pressure'], marker='o')

# Incorporate the other graph properties
plt.title('Pressure in World Cities')
plt.ylabel('Pressure (hPa)')
plt.xlabel('Longitude')
plt.grid(True)

# Save the figure
plt.savefig('PressureInWorldCities.png')

# Show plot
plt.show()
