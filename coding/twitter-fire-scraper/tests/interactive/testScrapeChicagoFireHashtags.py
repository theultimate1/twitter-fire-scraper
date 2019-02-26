"""
Demonstrates the ability to scrape tweets regarding chicago fires.
"""
# noinspection PyUnresolvedReferences
import os
from pprint import pprint

import __init__

import tweepy
from tweepy import FileCache, Status

import yaml
from config import DataConfig
from twitter import TwitterAuthentication, GEOBOX_CHICAGO
from util import geobox_to_geocode

if __name__ == "__main__":
    # Set up twitter auth.
    twauth = TwitterAuthentication()

    # Set up a file-based cache to avoid blasting the Twitter API too much.
    cache = FileCache(cache_dir="cache/")
    api = tweepy.API(twauth.oauth_handler, cache=cache)

    print(
    "Scraping the top 500 tweets that reference hashtags from our '{}' datafile 20 miles from the center of Chicago's geo-box.".format(
        os.path.basename(DataConfig.FIRE_HASHTAGS_DATA_PATH)))

    # Read hashtags from datafile.
    with open(DataConfig.FIRE_HASHTAGS_DATA_PATH) as f:
        fire_hashtags_data = yaml.load(f)

    hashtags = fire_hashtags_data['hashtags']

    print("Looking for {}...".format(', '.join('#' + hashtag for hashtag in hashtags)))

    geocode = geobox_to_geocode(GEOBOX_CHICAGO, "20mi")

    print(geocode)

    search = api.search(q='#pizza', geocode=geocode)

    print("Got {} back.".format(len(search)))

    for status in search:  # type: Status
        pprint(status.text)
