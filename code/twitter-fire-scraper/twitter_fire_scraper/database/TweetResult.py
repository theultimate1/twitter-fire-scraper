from tweepy import Status
from typing import Set


class TweetResult(object):

    def __init__(self, data: Status, tags: Set[str], relevancy: bool):
        self.data = data
        self.tags = tags
        self.relevancy = relevancy

    def get_id(self):
        return self.data.id