from __future__ import absolute_import

import os
from pprint import pprint

import twitter_fire_scraper
# This is needed to NOT import our source code locally, and force import of installed twitter-fire-scraper from PyPI.

from twitter_fire_scraper.scraper import TwitterAuthentication, Scraper
from twitter_fire_scraper.util import pretty_print_statuses

twauth = TwitterAuthentication(
    consumer_key="FILL ME IN!",
    consumer_secret="FILL ME IN!",
    access_token="FILL ME IN!",
    access_token_secret="FILL ME IN!",
)

# You normally initialize a scraper like this, but this is a demo,
# so we will be using a JSON file located at ~/secrets.json!
# scraper = Scraper(twitter_authentication=twauth)


# Initialize using secrets file. Demo only. Go fill in those keys!
# After that, comment me out.
scraper = Scraper(TwitterAuthentication.autodetect_twitter_auth())

results = scraper.scrape_terms({"pizza", "cake"}, count=3)

for term, statuses in results.items():
    print("{} hits for {}:".format(len(statuses), term))
    pretty_print_statuses(statuses)
