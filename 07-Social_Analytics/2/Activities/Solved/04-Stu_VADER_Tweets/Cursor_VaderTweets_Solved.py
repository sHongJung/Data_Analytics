# Dependencies
import tweepy
import json
import numpy as np

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Target User Account
target_user = "@DalaiLama"

# Variables for holding sentiments
compound_list = []
positive_list = []
negative_list = []
neutral_list = []

for page in tweepy.Cursor(api.user_timeline, id=target_user).pages(200):
    # page is a list of statuses
    page = page[0]
    tweet = json.dumps(page._json, indent=3)
    tweet = json.loads(tweet)
    text = tweet['text']
    print(text)
    # print(resp['text'])
    # print("----------")

    # Run Vader Analysis on each tweet
    compound = analyzer.polarity_scores(text)["compound"]
    pos = analyzer.polarity_scores(text)["pos"]
    neu = analyzer.polarity_scores(text)["neu"]
    neg = analyzer.polarity_scores(text)["neg"]

    # Add each value to the appropriate array
    compound_list.append(compound)
    positive_list.append(pos)
    negative_list.append(neg)
    neutral_list.append(neu)    


# Print the Averages
print("")
print("User: %s" % target_user)
print("Compound: %s" % np.mean(positive_list))
print("Positive: %s" % np.mean(positive_list))
print("Neutral: %s" % np.mean(neutral_list))
print("Negative: %s" % np.mean(negative_list))
