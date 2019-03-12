from __future__ import absolute_import
import twitter_fire_scraper
# This is needed to NOT import our source code locally, and force import of installed twitter-fire-scraper from PyPI.

from twitter_fire_scraper.scraper import TwitterAuthentication, Scraper

twauth = TwitterAuthentication(
    consumer_key="",
    consumer_secret="",
    access_token="",
    access_token_secret="",
)

scraper = Scraper(twitter_authentication=twauth)
