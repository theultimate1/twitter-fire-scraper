import unittest

from pymongo import MongoClient

from config import Config
from database.TweetResult import TweetResult, ERelevancy
from database.TweetResultDAO import TweetResultDAO
from tests.test.incur_api_hits.cached_tweets import CachedTweets
from util import status_from_dict


class TestDaoSimple(unittest.TestCase):

    def setUp(self) -> None:
        # connect to localhost
        self.client = MongoClient(Config.Defaults.MONGODB_CONNECTION_STRING)

        # make a DAO with our connection
        self.dao = TweetResultDAO(self.client, collection_name=self.__class__.__name__)

    def tearDown(self) -> None:
        self.client.close()

    def testRealData(self):
        """Tests that the DAO can successfully insert and delete a few real records."""
        self.assertTrue(True)  # TODO

    def testMockData(self):
        """Tests that the DAO can successfully insert and delete a single mock record."""

        # delete if it somehow exists
        if self.dao.get_by_id('test_id') is not None:
            self.dao.delete_by_id('test_id')

        # mock tweetresult
        tweetResult = TweetResult(
            data=status_from_dict({
                "id": "test_id",
                "full_text": "hello!"
            }),

            tags=["test", "deleteme"],
            relevancy=ERelevancy.IRRELEVANT)

        # save a tweetresult
        self.dao.save_one(tweetResult.serialize())

        result = self.dao.get_by_id("test_id")

        self.assertNotEqual(result, None)
        self.assertIsInstance(result, TweetResult)

        # delete it now
        self.dao.delete_by_id(result.get_id())

        # it should be None
        self.assertEqual(self.dao.get_by_id("test_id"), None)
