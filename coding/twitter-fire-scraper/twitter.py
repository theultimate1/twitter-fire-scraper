import tweepy
from pymongo import MongoClient
from tweepy import OAuthHandler, Status

from config import SecretsConfig
from models import Point

GEOBOX_WORLD = [Point(-180, -90), Point(180, 90)]

# From http://boundingbox.klokantech.com/
GEOBOX_CHICAGO = [Point(41.573604, -87.965887, ), Point(42.085967, -87.367663, )]


class TwitterAuthentication(object):
    """Twitter authentication object.

    This is basically just a wrapper for Twitter API keys to prevent a bunch of variables being scattered everywhere.
    """

    def __init__(self):
        self.consumer_key = SecretsConfig.CONSUMER_KEY
        self.consumer_secret = SecretsConfig.CONSUMER_SECRET
        self.access_token = SecretsConfig.ACCESS_TOKEN
        self.access_token_secret = SecretsConfig.ACCESS_TOKEN_SECRET

        self.oauth_handler = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.oauth_handler.set_access_token(self.access_token, self.access_token_secret)


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
            print("Relevant:")
            return True

        if verbose:
            # Show snapshot of irrelevant tweet
            print("Not relevant: {}".format(text))

        return False

    def on_status(self, status):
        # type: (SimpleFireStreamListener, Status) -> None

        if SimpleFireStreamListener.is_relevant(status, verbose=True):
            text = status.text

            print("Relevant: " + text.encode("UTF-8"))


class MongoDBStreamListener(tweepy.StreamListener):
    """A twitter stream listener that logs flagged tweets to a MongoDB database."""

    @staticmethod
    def is_relevant(status, verbose=False):
        # type: (Status, bool) -> bool
        """
        Tells you if a Status is relevant.
        :param status: The status.
        :param verbose: Should we print irrelevant statuses?
        :return: Whether or not the status is relevant.
        """

        if 'fire' in status.text:
            return True

        return False

    def __init__(self, database_name="MongoDBStreamListener"):
        super(MongoDBStreamListener, self).__init__()

        # MongoDB client.
        self.mongoclient = MongoClient(SecretsConfig.MONGODB_CONNECTION_STRING)

        # MongoDB database name.
        self.mongodatabase = self.mongoclient[database_name]

        # Table to which tweets are saved.
        self.TWEETS_TABLE = database_name

    # noinspection PyUnresolvedReferences
    def on_status(self, status):
        # type: (MongoDBStreamListener, Status) -> None

        # Make text safe to print in console.
        safe_text = status.text.encode('UTF-8')

        # If the status is relevant,
        if MongoDBStreamListener.is_relevant(status):
            # Insert it into our database.
            self.mongodatabase[self.TWEETS_TABLE].insert_one(status._json)
            print("Hit: " + safe_text)
        else:
            print("Ign: " + safe_text)
