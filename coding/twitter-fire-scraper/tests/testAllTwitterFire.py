"""
Demonstrates the ability to search for fire regardless of location.
"""

from pprint import pprint

import colorama

from twitter import TwitterAuthentication

# Set up twitter auth.
twauth = TwitterAuthentication()
api = twauth.get_api()

if __name__ == "__main__":
    print("Just searching for 'fire'... Probably not going to get us Chicago fire incidents, "
          "perhaps will get us SoundCloud tracks.")
    pprint([(status.text,) for status in api.search("fire")])
