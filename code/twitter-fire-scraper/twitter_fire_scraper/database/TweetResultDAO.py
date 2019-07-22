from flask_pymongo import PyMongo, MongoClient

from database import TweetResult

class TweetResultDAO(object):

    def __init__(self, mongoclient: MongoClient):

        self.collection_name = "tweets"

        self.mongoclient = mongoclient
        self.connection = self.mongoclient.tweets

    def save_one(self, tweetresult: TweetResult):
        self.connection[self.collection_name].save(tweetresult)
