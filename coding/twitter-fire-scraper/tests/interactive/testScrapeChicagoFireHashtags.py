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
from twitter import TwitterAuthentication, GEOBOX_CHICAGO
from util import geobox_to_geocode


def get_fire_search_terms():
    # Read hashtags from datafile.
    with open(DataConfig.FIRE_HASHTAGS_DATA_PATH) as f:
        fire_hashtags_data = yaml.load(f)
        return fire_hashtags_data['hashtags']


if __name__ == "__main__":

    # Maximum tweets to search for.
    MAX_TWEETS = 10

    # Radius to search for tweets in.
    TWEET_RADIUS = "50mi"

    # Set up twitter auth.
    twauth = TwitterAuthentication()

    # Set up a file-based cache to avoid blasting the Twitter API too much.
    # cache = FileCache(cache_dir="cache/")
    api = tweepy.API(twauth.oauth_handler, )

    # Get Twitter geocode from Chicago's geobox.
    geocode = geobox_to_geocode(GEOBOX_CHICAGO, TWEET_RADIUS)

    # List of search terms to search for.
    search_terms = get_fire_search_terms()

    print(
        "Scraping the top {n} tweets that reference search terms from our '{path}' datafile inside {geocode}".format(
            n=MAX_TWEETS, path=os.path.basename(DataConfig.FIRE_HASHTAGS_DATA_PATH), geocode=geocode))

    # All tweets, sorted by search term
    all_tweets = {}

    # For all search terms,
    for search_term in search_terms:  # type: str

        # Conduct a search.
        cursor = tweepy.Cursor(api.search, q=search_term)

        # Retrieve however many tweets we want, and store that in our dictionary.
        all_tweets[search_term] = [status for status in cursor.items(MAX_TWEETS)]

        print("{n} hits for {ht}:".format(n=len(all_tweets[search_term]), ht=search_term))

        # For all statuses that we retrieved,
        for status in all_tweets[search_term][0:5]:  # type: Status
            print(" " * 4),  # Prefix with four spaces to show hierarchy.
            print("<https://www.twitter.com/statuses/{id}> :".format(id=str(status.id)))  # URL of tweet.

            print(" " * 4),  # Status belonging to URL.
            print(status.text.encode("UTF-8"))  # Status text.
            print

    print("Final results of scraping {n} tweets each from these search terms:".format(
        n=MAX_TWEETS))

    print(", ".join(search_terms))

    # Determine unique statuses found from all keywords

    # Unique statuses. Sets can contain no duplicate elements.
    unique_status_ids = set()  # type: set[long]
    total_statuses = 0  # Total amount of statuses found.
    for keyword, statuses in all_tweets.items():

        for status in statuses:
            unique_status_ids.add(status.id)  # Add the ID as it can be enumerated in a set and is unique.
            total_statuses += 1  # 1 more status!

    for keyword, statuses in all_tweets.items():
        print("{keyword:20s}: {n} hits".format(keyword=keyword, n=len(statuses)))

    print("{uq} unique statuses out of {tot} total statuses".format(
        uq=len(unique_status_ids), tot=total_statuses))
