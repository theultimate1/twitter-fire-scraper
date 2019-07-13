from flask_pymongo import PyMongo, MongoClient

from twitter_fire_scraper.database import TweetResult

class TweetResultDAO(object):

    def __init__(self, mongoclient: MongoClient):
        self.mongoclient = mongoclient
        self.connection = self.mongoclient.tweets

    def save_one(self, collection: str, tweetresult: TweetResult):
        self.connection[collection].save(tweetresult)
