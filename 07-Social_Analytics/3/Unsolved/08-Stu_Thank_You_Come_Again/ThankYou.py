# Dependencies
import tweepy
import time
import json

# Twitter API Keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Target Term
target_term = "@DaDataBootcamp"

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

    # @TODO Loop through all tweets
    # CODE HERE

        # @TODO Get ID and Author of most recent tweet directed to me
        # CODE HERE

        # @TODO Print the tweet_id
        # CODE HERE

        # @TODO Use Try-Except to avoid the duplicate error
        try:
        # CODE HERE

            # Print success message
            # CODE HERE
        except Exception:            
        # CODE HERE

        # @TODO Print message to signify complete cycle
        # CODE HERE


# @TODO Set timer to run every minute

