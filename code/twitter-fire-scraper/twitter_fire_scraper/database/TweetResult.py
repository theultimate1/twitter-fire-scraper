from enum import Enum

from tweepy import Status
from typing import Set


class ERelevancy(Enum):
    """An enumeration that represents if something is uncategorized, relevant, or irrelevant."""
    UNCATEGORIZED = 1
    RELEVANT = 2
    IRRELEVANT = 3


class TweetResult(object):

    def __init__(self, data: Status, tags: Set[str], relevancy: ERelevancy):
        self.data = data
        self.tags = tags
        self.relevancy = relevancy

    def get_id(self):
        """The ID of a Tweet. This is unique."""
        return self.data.id

    def get_text(self):
        """The content of a tweet.

        Returns either "full_text" or "text", favoring the former as it is longer."""
        if 'full_text' in self.data:
            return self.data['full_text']

        elif 'text' in self.data:
            return self.data['text']

        else:
            raise KeyError("Tweet has no text!")

    def serialize_to_dict(self):
        """Serialize this TweetResult object to a JSON-like object that can be saved to a MongoDB database"""
        return {
            'data': self.data,
            '_id': self.get_id(),
            'tags': self.tags,
            'relevancy': self.relevancy
        }
