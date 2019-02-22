"""
A file that contains utilities to detect if a hashtag refers to a disaster, as well as disaster hashtag-generating
utilities.
"""


def contains_hashtag(text, hashtag):
    # type: (str, str) -> bool
    """Tells you if text contains a hashtag.

    :param text: Text to search in.
    :param hashtag: Hashtag to search for.
    :return: If the hashtag exists in the text.
    """

    if hashtag[0] == '#':
        hashtag = hashtag[1:]

    return ("#" + hashtag).lower() in text.lower()
