from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from config import Config
from database.TweetResult import TweetResult, ERelevancy


class TweetResultDAO(object):
    """
    A DAO that lets you save, modify, and retrieve TweetResults from the database.
    """

    def __init__(self, mongoclient: MongoClient):
        self.client: MongoClient = mongoclient
        self.db: Database = self.client.tweets
        self.collection: Collection = self.db['all_tweets']

    def save_one(self, tweetresult: TweetResult):
        """Save a single TweetResult object."""
        self.collection.insert_one(tweetresult)

    def get_by_id(self, id: int):
        return self.collection.find({"_id": id})


# testing
if __name__ == '__main__':
    # connect to localhost
    client = MongoClient(Config.Defaults.MONGODB_CONNECTION_STRING)

    # make a DAO with our connection
    dao = TweetResultDAO(client)

    dao.save_one(TweetResult(data={
        "id": "test",
        "full_text": "hello!",
        "tags": {}
    },
        tags={"test"},
        relevancy=ERelevancy.IRRELEVANT))

    print(dao.get_by_id())
