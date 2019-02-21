import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

from config import Config

class Tweet(object):
    def __init__(self, poster, message, retweet=False):
        self.poster = poster
        self.message = message

class TwitterClient(object):
    '''
    Generic Twitter Class for the App
    '''

    def __init__(self):
        # keys and tokens for Twitter
        consumer_key = Config.CONSUMER_KEY
        consumer_secret = Config.CONSUMER_SECRET
        access_token = Config.ACCESS_TOKEN
        access_token_secret = Config.ACCESS_TOKEN_SECRET

        # Attempting authentication
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    @staticmethod
    def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    @staticmethod
    def get_tweet_sentiment(tweet):
        # thresholds to classify pos and neg
        POS_THRESH = 0.2
        NEG_THRESH = 0
        analysis = TextBlob(TwitterClient.clean_tweet(tweet))
        if analysis.sentiment.polarity > POS_THRESH:
            return 'positive'
        elif analysis.sentiment.polarity < NEG_THRESH:
            return 'negative'
        else:
            return 'neutral'

    def get_tweets(self):
        return "nope."