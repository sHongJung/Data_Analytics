# Dependencies
import tweepy
import time
import json
import twitter_api as ta
from pprint import pprint

# Twitter API Keys
consumer_key = ta.consumer_key
consumer_secret = ta.consumer_secret
access_token = ta.access_token
access_token_secret = ta.access_token_secret

# Target Term
target_term = "@PyBootCoding"

# Opening message
print("We're going live, sir!")

# Create Thank You Function
def ThankYou():

    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # @TODO Search for all tweets
    # CODE HERE
    tweets = api.home_timeline()
   # pprint(tweets)

    # @TODO Loop through all tweets
    # CODE HERE
    #for tweet in tweets:

        # @TODO Get ID and Author of most recent tweet directed to me
        # CODE HERE
    mr_id = tweets[0]['entities']['user_mentions'][0]['screen_name']
    mr_name = tweets[0]['entities']['user_mentions'][0]['name']

        # @TODO Print the tweet_id
        # CODE HERE
    print(mr_name)
        # @TODO Use Try-Except to avoid the duplicate error
    try:
        # CODE HERE
        api.update_status(f"Thank you @{mr_id}, Come again {mr_name}!")
            # Print success message
            # CODE HERE
        print("The message is tweeted successfully, sir!")
    except Exception:
        # CODE HERE
        print("dup!")

        # @TODO Print message to signify complete cycle
        # CODE HERE


# @TODO Set timer to run every minute

ThankYou()