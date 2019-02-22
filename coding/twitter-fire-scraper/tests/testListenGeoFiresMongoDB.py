"""
Demonstrates the ability to listen in a geographical area for a keyword tweet and save it to a MongoDB database.
"""
import os
import sys

# Append parent directory to enhance portability.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tweepy

from twitter import TwitterAuthentication, MongoDBStreamListener, GEOBOX_CHICAGO

if __name__ == "__main__":
    # Set up twitter auth.
    twauth = TwitterAuthentication()
    api = twauth.get_api()

    print("Listening for fires and logging to a MongoDB database.")
    mongolistener = MongoDBStreamListener()
    mongostream = tweepy.Stream(auth=api.auth, listener=mongolistener)

    mongostream.filter(locations=GEOBOX_CHICAGO)
