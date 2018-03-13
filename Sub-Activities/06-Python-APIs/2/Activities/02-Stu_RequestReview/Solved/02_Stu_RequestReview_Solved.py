# Dependencies
import json
import requests as req

# Specify the URL
url = "http://nyt-mongo-scraper.herokuapp.com/api/headlines"

# Make request and store response
response = req.get(url)

# Print status code
print(response.status_code)

# Parse the JSON response
response_json = response.json()

# Print the JSON representations of the first and last posts
print("The first response is " + json.dumps(response_json[0], indent=2) + ".")
print("The last response is " + json.dumps(response_json[-1], indent=2) + ".")

# Print number of articles we received
print("We received " + str(len(response_json)) + " responses.")
