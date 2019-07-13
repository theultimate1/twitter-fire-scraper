from tweepy import Status
from typing import Set


class TweetResult(object):

    def __init__(self, data: Status, tags: Set[str], relevancy: bool):
        self.data = data
        self.id = self.data.id
        self.tags = tags
        self.relevancy = relevancy

    def serialize_to_dict(self):
        """Serialize this TweetResult object to a dictionary that can be saved in a BSON format (like JSON)"""
        return {
            'data': self.data,
            'id': self.id,
            'tags': self.tags,
            'relevancy': self.relevancy
        }
