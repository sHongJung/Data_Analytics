# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime
import twitter_api as ta
from pprint import pprint

# Twitter API Keys

# Weather API

# Create a function that gets the weather in London and Tweets it
def WeatherTweet(city):
    """Get Weather in London and Tweet it out."""
    # @TODO: Construct a Query URL for the OpenWeatherMap
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
    parameters = {'APPID':api_key, 'q':city, 'units':'metric'}

    # @TODO: Perform the API call to get the weather
    weather_json = req.get(url, params=parameters).json()

    # @TODO: Twitter credentials
    consumer_key = ta.consumer_key
    consumer_secret = ta.consumer_secret
    access_token = ta.access_token
    access_token_secret = ta.access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

   # @TODO: Tweet the weather
    Temperature = weather_json['main']['temp']
    api.update_status(f'Temperature of {city} is {Temperature}˚C now.')
    # @TODO: Print success message
    print(f'Temperature of {city} is tweeted successfully!')


# @TODO: Set timer to run every 1 hour
while(1):
    WeatherTweet('San Francisco')
    time.sleep(3600)