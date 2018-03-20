# Create code to answer each of the following questions.
# Hint: You will need multiple target urls and multiple API requests.

# Dependencies
import requests
import json

# Google API Key
gkey = "AIzaSyA_Clyz3478YAUnsESNHE5dyktvvMoa-vw"

# ------------------------------------------------------------------------------

# 1. What are the geocordinates (latitude and longitude) of Seattle,
# Washington?
target_city = "Seattle, Washington"

# Build URL using the Google Maps API
target_url = "https://maps.googleapis.com/maps/api/geocode/json" \
    "?address=%s&key=%s" % (target_city, gkey)

print("\r\nDrill #1")
print(target_url)

# Run request
seattle_geo = requests.get(target_url).json()

# Extract Lat/Lng
lat = seattle_geo["results"][0]["geometry"]["location"]["lat"]
lng = seattle_geo["results"][0]["geometry"]["location"]["lng"]

# Print results
print("%s: %s, %s" % (target_city, lat, lng))

# ------------------------------------------------------------------------------

# 2. What are the geocordinates (latitude and longitude) of The White House?
target_city = "The White House"

# Build URL using the Google Maps API
target_url = "https://maps.googleapis.com/maps/api/geocode/json" \
    "?address=%s&key=%s" % (target_city, gkey)

print("\r\nDrill #2")
print(target_url)

# Run request
dc_geo = requests.get(target_url).json()

# Extract Lat/Lng
lat = dc_geo["results"][0]["geometry"]["location"]["lat"]
lng = dc_geo["results"][0]["geometry"]["location"]["lng"]

# Print results
print("%s: %s, %s" % (target_city, lat, lng))

# ------------------------------------------------------------------------------

# 3. Find the names and addresses of a bike store in Seattle, Washington.
#    Hint: See https://developers.google.com/places/web-service/supported_types
target_type = "bicycle_store"
seattle_lat = 47.6062095
seattle_lng = -122.3320708

# Build URL using the Google Maps API
target_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json" \
    "?location=%s,%s&types=%s&radius=%s&key=%s" % (
        seattle_lat, seattle_lng, target_type, 8000, gkey)

print("\r\nDrill #3")
print(target_url)

# Run request
seattle_bikes = requests.get(target_url).json()

# Print the json (pretty printed)
# print(json.dumps(seattle_bikes, indent=4, sort_keys=True))

# Print the name and address of the first bike shop to appear
print(seattle_bikes["results"][0]["name"])
print(seattle_bikes["results"][0]["vicinity"])

# ------------------------------------------------------------------------------

# 4. Find a balloon store near the White House.
target_search = "Balloon Store"
dc_lat = 38.8976763
dc_lng = -77.0365298

# Build URL using the Google Maps API
target_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json" \
    "?location=%s,%s&keyword=%s&radius=%s&key=%s" % (
        dc_lat, dc_lng, target_search, 8000, gkey)

print("\r\nDrill #4")
print(target_url)

# Run request
dc_balloons = requests.get(target_url).json()

# Print the json (pretty printed)
# print(json.dumps(dc_balloons, indent=4, sort_keys=True))

# Print the name and address of the first baloon shop that appears
print(dc_balloons["results"][0]["name"])
print(dc_balloons["results"][0]["vicinity"])

# ------------------------------------------------------------------------------

# 5. Find the nearest dentist to your house.
# Hint: Use Google Maps to find your latitude and Google Places to find
# the dentist. You may also need the rankby property.
my_address = "151 Sip Ave"
target_search = "dentist"
target_url = "https://maps.googleapis.com/maps/api/geocode/json" \
    "?address=%s&key=%s" % (my_address, gkey)

print("\r\nDrill #5")
print(target_url)

my_geo = requests.get(target_url).json()
lat = my_geo["results"][0]["geometry"]["location"]["lat"]
lng = my_geo["results"][0]["geometry"]["location"]["lng"]

# print(lat)
# print(lng)
target_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json" \
    "?location=%s,%s&types=%s&rankby=distance&key=%s" % (
        lat, lng, target_search, gkey)

print(target_url)

# Run request
my_dentist = requests.get(target_url).json()

# Print the json (pretty printed)
# print(json.dumps(my_dentist, indent=4, sort_keys=True))

# Print the name and address of the first baloon shop that appears
print(my_dentist["results"][0]["name"])
print(my_dentist["results"][0]["vicinity"])

# ------------------------------------------------------------------------------


# 6. Bonus: Find the names and addresses of the top five places Google suggests
# for the phrase: "Happy Place ". Hint: Read about "Text Search Results"
# (https://developers.google.com/places/web-service/search#TextSearchRequests)
my_phrase = "Happy Place"
target_url = "https://maps.googleapis.com/maps/api/place/textsearch/json" \
    "?query=%s&key=%s" % (my_phrase, gkey)

print("\r\nDrill #6")
print(target_url)

happy_places = requests.get(target_url).json()
print(happy_places)
# print(json.dumps(happy_places, indent=4, sort_keys=True))

for place in range(5):
    print(happy_places["results"][place]["name"])
    print(happy_places["results"][place]["formatted_address"])
