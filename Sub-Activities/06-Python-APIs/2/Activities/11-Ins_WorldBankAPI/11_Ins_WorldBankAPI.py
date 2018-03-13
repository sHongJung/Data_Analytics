# Dependencies
import json
import requests as req

url = 'http://api.worldbank.org/v2/'
params = {'format': 'json'}

# Get country information in JSON format
countries_response = req.get(url + 'countries', params=params).json()

# Pretty print the response
print(json.dumps(countries_response, indent=4))

# First element is general information, second is countries themselves
countries = countries_response[1]

# Report the names
for country in countries:
    print(country['name'])
