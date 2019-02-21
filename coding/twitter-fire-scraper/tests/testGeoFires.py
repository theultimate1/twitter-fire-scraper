"""
Demonstrates the ability to listen in a geo-location for the keyword 'fire'.
"""

import time

import tweepy

from twitter import SimpleFireStreamListener, TwitterAuthentication, GEOBOX_CHICAGO

if __name__ == "__main__":

    # Set up twitter auth.
    twauth = TwitterAuthentication()
    api = twauth.get_api()

    print("Using our simple 'fire' stream listener, let's see what Chicago geotagged tweets have 'fire' in them.")

    simpleFireStreamListener = SimpleFireStreamListener()
    simpleFireStream = tweepy.Stream(auth=api.auth, listener=simpleFireStreamListener)

    print("Streaming for 60 seconds.")
    simpleFireStream.filter(locations=GEOBOX_CHICAGO, async=True)
    try:
        time.sleep(60)
    except KeyboardInterrupt:
        simpleFireStream.disconnect()
    finally:
        simpleFireStream.disconnect()

    print("As you can see, either none or few of these tweets actually contain the word 'fire'.")