import tweepy
import datetime

# set up Twitter API credentials
consumer_key = "TOKEN"
consumer_secret = "TOKEN"
access_token = "TOKEN"
access_token_secret = "TOKEN"

# authenticate with the Twitter API
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# compose the tweet with the current date
date = datetime.datetime.now().strftime("%m/%d/%Y")
tweet = f"Today's date is {date}."

# post the tweet
api.update_status(tweet)
