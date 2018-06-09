# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Quotes to Tweet
Quotes_list = ["Quote1", "Quote2", "Quote3", "Quote4"]

# Create a function that tweets
# Create function for tweeting
def tweet_out(counter):
    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    
    # Tweet the next quote
    api.update_status(Quotes_list[counter])

    # Print success message
    print("Tweeted Successfully")

counter = 0
# Set timer to run every minute
while(counter < len(Quotes_list)):
    tweet_out(counter)
    time.sleep(10)
    counter += 1