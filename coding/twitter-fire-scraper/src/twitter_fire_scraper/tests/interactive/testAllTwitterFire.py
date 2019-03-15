"""
Demonstrates the ability to search for fire regardless of location.
"""
# noinspection PyUnresolvedReferences
import __init__

import tweepy

from pprint import pprint

from twitter import TwitterAuthentication

if __name__ == "__main__":
    # Set up twitter auth.
    twauth = TwitterAuthentication.autodetect_twitter_auth()
    api = tweepy.API(twauth.oauth_handler)

    print("Just searching for 'fire'... Probably not going to get us Chicago fire incidents.")

    for status in api.search("fire"):
        print(status.text)