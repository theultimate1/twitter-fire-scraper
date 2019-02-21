import re
import threading
import time
from pprint import pprint

import colorama
import tweepy
from colorama import Fore
from tweepy import OAuthHandler, Status
from textblob import TextBlob

from config import Config
from util import colorama_highlight_red, colorama_reset

GEOBOX_WORLD = [-180, -90, 180, 90]

# From http://boundingbox.klokantech.com/
GEOBOX_CHICAGO = [-87.965887, 41.573604, -87.367663, 42.085967]


class TwitterAuthentication(object):
    """Twitter authentication object."""

    def __init__(self):
        self.consumer_key = Config.CONSUMER_KEY
        self.consumer_secret = Config.CONSUMER_SECRET
        self.access_token = Config.ACCESS_TOKEN
        self.access_token_secret = Config.ACCESS_TOKEN_SECRET

        self.oauth_handler = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.oauth_handler.set_access_token(self.access_token, self.access_token_secret)

    def get_api(self):
        """Generates a Tweepy API object."""
        return tweepy.API(self.oauth_handler)


class TwitterClient(object):
    '''
    Generic Twitter Class for the App
    '''

    def __init__(self):

        self.twitter_auth = TwitterAuthentication()

        self.api = self.twitter_auth.get_api()

    @staticmethod
    def clean_tweet(tweet):
        # type: (str) -> str
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    @staticmethod
    def get_tweet_sentiment(tweet):
        # type: (str) -> str

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


class MongoDBFileStreamListener(tweepy.StreamListener):
    """A twitter stream listener that logs flagged tweets to a MongoDB database."""

    # TODO implement it :)


# override tweepy.StreamListener to add logic to on_status
class SimpleFireStreamListener(tweepy.StreamListener):
    """A naive twitter stream listener that only watches for the phrase "fire".
    This is a simple demo and is best used on the command-line."""

    @staticmethod
    def is_relevant(status, verbose=False):
        # type: (Status, bool) -> bool
        """
        Tells you if a Status is relevant.
        :param status: The status.
        :param verbose: Should we print irrelevant statuses?
        :return: Whether or not the status is relevant.
        """

        text = status.text.encode("UTF-8")

        if 'fire' in text:
            return True

        if verbose:
            # Show snapshot of irrelevant tweet
            print("Not relevant: {}".format(text.replace("\n", "\\n").replace("\r", "\\r")[0:50] + "..."))
            colorama_reset()

        return False

    def on_status(self, status):

        if SimpleFireStreamListener.is_relevant(status, verbose=True):
            text = status.text

            # Make it pop out.
            text = colorama_highlight_red(text, "fire")

            print(text.encode("UTF-8"))


if __name__ == "__main__":
    """Does some tests if you run this file directly."""

    # Set up terminal color.
    colorama.init()

    tc = TwitterClient()
    twauth = TwitterAuthentication()
    api = twauth.get_api()


    def firesDemo():

        print("Just searching for 'fire'... Probably not going to get us Chicago fire incidents, "
              "perhaps will get us SoundCloud tracks.")
        pprint([(status.text,) for status in tc.api.search("fire")])


    def geoFiresDemo():
        print("Using our simple 'fire' stream listener, let's see what Chicago geotagged tweets have 'fire' in them.")

        simpleFireStreamListener = SimpleFireStreamListener()
        simpleFireStream = tweepy.Stream(auth=api.auth, listener=simpleFireStreamListener)

        print("Streaming for 60 seconds.")
        simpleFireStream.filter(locations=GEOBOX_CHICAGO, async=True)
        try:
            time.sleep(60)
        except KeyboardInterrupt:
            simpleFireStream.disconnect()
        finally:
            simpleFireStream.disconnect()

        print("As you can see, either none or few of these tweets actually contain the word 'fire'.")


    firesDemo()

    geoFiresDemo()
