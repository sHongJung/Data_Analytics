# Dependencies
import requests as req

# Define URL and query parameters
url = "http://api.worldbank.org/v2/"
params = {'format': 'json'}

# Get the list of lending types the world bank has
response = req.get(url + "lendingTypes", params=params).json()
lending_types = [lending_type["id"] for lending_type in response[1]]

# Next, determine how many countries fall into each lending type.
# Hint: Look at the first element of the response list to get the
# total number of countries per lending type.

country_count_by_type = {}
for lending_type in lending_types:
    # Add `lendingType` query parameter
    params['lendingType'] = lending_type
    # Send GET request
    response = req.get(url + "countries", params=params).json()
    # Get total number of countries per lending type
    total = response[0]["total"]
    country_count_by_type[lending_type] = total

# Print the number of countries of each lending type
for lending_type, count in country_count_by_type.items():
    print("The number of countries with lending type " + lending_type +
          " is " + str(count) + ".")
