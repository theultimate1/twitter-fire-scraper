"""
Demonstrates the ability to scrape tweets regarding chicago fires, and store them in a MongoDB database.
"""
# noinspection PyUnresolvedReferences
import os
from pprint import pprint

import __init__

import tweepy
from tweepy import FileCache, Status

import yaml
from config import DataConfig
from hashtags import ensure_hashtag
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

    for hashtag in hashtags:  # type: str
        # For all hashtags,
        hashtag = ensure_hashtag(hashtag)

        # Conduct a search.
        search = api.search(q=hashtag, geocode=geocode)

        print("{n} hits for {ht}:".format(n=len(search), ht=hashtag))

        for status in search[0:5]:  # type: Status
            print(" " * 4),  # Prefix with four spaces to show hierarchy.
            pprint(status.text)
