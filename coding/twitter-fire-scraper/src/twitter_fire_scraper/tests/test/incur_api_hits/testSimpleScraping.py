import unittest

from scraper import Scraper
from twitter import TwitterAuthentication


class TestSimpleScraping(unittest.TestCase):

    def testCanScrapeTerm(self):
        """Tests that scraper can scrape one term."""

        twauth = TwitterAuthentication.autodetect_twitter_auth()

        scraper = Scraper(twitter_authentication=twauth)

        results = scraper.scrape_terms({"potato"}, count=1)

        assert (len(results.keys()) == 1)

        assert (isinstance(results['potato'][0].text, str))

    def testCanScrapeAccount(self):
        """Tests that scraper can scrape one account."""
        twauth = TwitterAuthentication.autodetect_twitter_auth()

        scraper = Scraper(twitter_authentication=twauth)

        results = scraper.scrape_accounts({"@redcross"}, count=1)

        assert (len(results.keys() == 1))

        assert (isinstance(results['@redcross'].text, str))
