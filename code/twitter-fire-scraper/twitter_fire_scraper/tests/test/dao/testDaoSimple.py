import unittest

from pymongo import MongoClient

from config import Config
from database.TweetResult import TweetResult, ERelevancy
from database.TweetResultDAO import TweetResultDAO


class TestDaoSimple(unittest.TestCase):

    def testSimple(self):
        """Tests that the DAO can successfully insert and delete a single record"""
        # connect to localhost
        client = MongoClient(Config.Defaults.MONGODB_CONNECTION_STRING)

        # make a DAO with our connection
        dao = TweetResultDAO(client, collection_name="test")

        # delete if it somehow exists
        if dao.get_by_id('test_id') is not None:
            dao.delete_by_id('test_id')

        # mock tweetresult
        tweetResult = TweetResult(
            data={
                "id": "test_id",
                "full_text": "hello!"
            },

            tags={"test"},
            relevancy=ERelevancy.IRRELEVANT)

        # save a tweetresult
        dao.save_one(tweetResult.serialize())

        result = dao.get_by_id("test_id")

        self.assertNotEqual(result, None)
        self.assertIsInstance(result, TweetResult)

        # delete it now
        dao.delete_by_id(result.get_id())

        # it should be None
        self.assertEqual(dao.get_by_id("test_id"), None)
