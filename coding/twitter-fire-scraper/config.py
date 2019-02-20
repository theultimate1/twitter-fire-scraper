import json
import os


def try_get(object, key):
    """Tries to get the value of a key in an object, and politely notifies you if it cannot find it."""

    if key not in object:
        raise KeyError("Could not find " + key + " inside of " + object + "! Does it exist?")

    return object[key]


class Config:
    # Path to secrets.
    SECRETS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "secrets.json")

    # Load secrets JSON into dictlike object.

    with open(SECRETS_PATH) as file:
        _json_object = json.load(file)

    # The Movie Database API Key
    TMDB_API_KEY = try_get(_json_object, 'tmdb_api_key')

    # Twitter username.
    TWITTER_HANDLE = try_get(_json_object, 'twitter_handle')

    # Twitter API keys.
    CONSUMER_KEY = try_get(_json_object, 'consumer_key')
    CONSUMER_SECRET = try_get(_json_object, 'consumer_secret')
    ACCESS_TOKEN = try_get(_json_object, 'access_token')
    ACCESS_TOKEN_SECRET = try_get(_json_object, 'access_token_secret')
