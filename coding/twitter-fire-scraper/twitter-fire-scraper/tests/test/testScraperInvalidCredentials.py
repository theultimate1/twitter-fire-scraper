"""
This file tests that the scraper fails correctly with invalid credentials.
"""
import unittest
from pprint import pprint

from tweepy import TweepError

from scraper import Scraper
from twitter import TwitterAuthentication
from util import flatten_status_dict

class TestInvalidCredentials(unittest.TestCase):

    def test_invalid(self):
        # This is one way to ideally initialize a Scraper object.
        scraper = Scraper(twitter_authentication=TwitterAuthentication(
            consumer_key="i4m4c0ns4m3r",
            consumer_secret="itsasecret",
            access_token="chuckecheesetokens?",
            access_token_secret="ticketmuncherdoesn'twork"
        ))

        terms = {"#pizza", "pizza", 'cat', '#cat'}

        try:
            results = scraper.scrape_terms(terms=terms, count=3)
        except TweepError as e:
            print("Failed with bogus credentials.")
            exit(0)

        raise Exception("Credentials should fail to validate.")

        results = flatten_status_dict(results)

        print("{} on all of twitter:".format(", ".join(terms)))
        pprint(results)
