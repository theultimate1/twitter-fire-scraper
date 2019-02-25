# coding=utf-8
import unittest

# noinspection PyUnresolvedReferences
import __init__
from hashtags import contains_hashtag, extract_hashtags


class TestHashtags(unittest.TestCase):

    def test_extract(self):
        assert (extract_hashtags("I love the #beach and #sand!") == {"#beach", "#sand"})

        assert (extract_hashtags(u"Pizza is so good! #~# 🍕") == set())

        assert (extract_hashtags("Man, Hashtags (#) are # nice # to # use # as # list # columns!") == set())

    def test_simple_contains(self):
        assert (contains_hashtag('I enjoy #swimming!', 'swimming'))
        assert (contains_hashtag('I enjoy #swimming so much!', 'swimming'))

        assert (not (contains_hashtag("I dislike #coldswimming.", "#swimming")))
        assert (not (contains_hashtag("I dislike #coldswimming.", "#cold")))
        assert (contains_hashtag("I dislike #coldswimming.", "#coldswimming"))
