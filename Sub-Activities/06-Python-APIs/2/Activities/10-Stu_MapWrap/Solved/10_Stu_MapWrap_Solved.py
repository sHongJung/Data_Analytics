# Dependencies
import os
import openweathermapy as ow
import pandas as pd
import apikeys

# Create a variable with your API key
api_key = apikeys.OWM_API_KEY

# Read list of cities
path = os.path.join('..', 'Resources', 'cities.csv')
cities = pd.read_csv(path, names=['Cities'])['Cities']
print(cities)

weather_data = []
data = []
# Loop through cities
for city in cities:
    # Get current data for each city
    response = ow.get_current(city, units="imperial", appid=api_key)
    # Add data to `weather_data` list
    weather_data.append(response)
    # Retrieve temperature, latitude and longitude
    city_data = response('main.temp', 'coord.lat', 'coord.lon')
    # Add temperature, latitude and longitude to `data` list
    data.append(city_data)

# Create a Pandas DataFrame with the results
column_names = ['Temperature', 'Latitude', 'Longitude']
cities_weather_df = pd.DataFrame(data, index=cities, columns=column_names)
print(cities_weather_df)
