from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

from config import Config
from database.TweetResult import TweetResult, ERelevancy


class TweetResultDAO(object):
    """
    A DAO that lets you save, modify, and retrieve TweetResults from the database.
    """

    def __init__(self, mongoclient: MongoClient, database_name='tweets', collection_name='all_tweets'):
        self.client: MongoClient = mongoclient

        self.database_name = database_name
        self.db: Database = self.client[self.database_name]

        self.collection_name = collection_name
        self.collection: Collection = self.db[self.collection_name]

    def save_one(self, tweetresult: TweetResult):
        """Save a single TweetResult object."""
        self.collection.insert_one(tweetresult)

    def get_by_id(self, id) -> TweetResult:
        cursor = self.collection.find({"_id": id})

        if cursor.count() == 0:
            raise ValueError("No tweet by that ID exists!")

        result = cursor.next()

        cursor.close()

        return TweetResult.deserialize(result)

    def delete_by_id(self, id):
        self.collection.delete_one({"_id": id})


# testing
if __name__ == '__main__':
    # connect to localhost
    client = MongoClient(Config.Defaults.MONGODB_CONNECTION_STRING)

    # make a DAO with our connection
    dao = TweetResultDAO(client, collection_name="test")

    # delete if it somehow exists
    if dao.get_by_id('test_id') is not None:
        dao.delete_by_id('test_id')

    # save a tweetresult
    dao.save_one(
        TweetResult(
            data={
                "id": "test_id",
                "full_text": "hello!"
            },

            tags={"test"},
            relevancy=ERelevancy.IRRELEVANT)
            .serialize()
    )

    print(dao.get_by_id("test_id"))
