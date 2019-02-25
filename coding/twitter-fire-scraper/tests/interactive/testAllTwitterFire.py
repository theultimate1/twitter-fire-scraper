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
    twauth = TwitterAuthentication()
    api = tweepy.API(twauth.oauth_handler)

    print("Just searching for 'fire'... Probably not going to get us Chicago fire incidents, "
          "perhaps will get us SoundCloud tracks.")
    pprint([(status.text,) for status in api.search("fire")])
