import os
import shutil
import unittest
import tempfile

import twitter_fire_scraper

from twitter_fire_scraper.models import Point
from twitter_fire_scraper.scraper import Scraper
from twitter_fire_scraper.tests.test.incur_api_hits.cached_tweets import CachedTweets
from twitter_fire_scraper.twitter import TwitterAuthentication
from twitter_fire_scraper.util import flatten_points, geobox_to_geocode


class TestFileSaving(unittest.TestCase):

    def setUp(self):
        # Temp folder for CSV files
        self.temp_folder = os.path.join(tempfile.gettempdir(), twitter_fire_scraper.__name__, TestFileSaving.__name__)

        # Scraper for scraping
        self.scraper = CachedTweets.scraper

        # Clean out temp folder
        if os.path.exists(self.temp_folder):
            shutil.rmtree(self.temp_folder)

        # Assorted filetype dirs
        self.csv_folder = os.path.join(self.temp_folder, 'csv')
        self.json_folder = os.path.join(self.temp_folder, 'json')

        os.makedirs(self.temp_folder)
        os.makedirs(self.csv_folder)
        os.makedirs(self.json_folder)

    def testSaveCSVSmall(self):
        """Tests that the scraper can produce CSV files."""
        tweets = CachedTweets.tweets_small()

        tweets_small_csv = os.path.join(self.csv_folder, 'tweets_small.csv')

        self.scraper.save_statusdict_to_csv(tweets, tweets_small_csv)

        with open(tweets_small_csv, 'r') as csv_file:

            line = csv_file.readline()
            assert ',' in line
