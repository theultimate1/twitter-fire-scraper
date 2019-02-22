"""
Demonstrates the ability to search for fire regardless of location.
"""
import os
import sys

# Append parent directory to enhance portability.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pprint import pprint

from twitter import TwitterAuthentication

# Set up twitter auth.
twauth = TwitterAuthentication()
api = twauth.get_api()

if __name__ == "__main__":
    print("Just searching for 'fire'... Probably not going to get us Chicago fire incidents, "
          "perhaps will get us SoundCloud tracks.")
    pprint([(status.text,) for status in api.search("fire")])
