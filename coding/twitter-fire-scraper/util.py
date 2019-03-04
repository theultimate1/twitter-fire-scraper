import colorama
from tweepy import Status
from typing import Dict, Set

from models import Point


def status_to_url(status):
    # type: (Status) -> str
    """Given a Status, return that status' url."""
    return "https://www.twitter.com/statuses/{id}".format(id=status.id)


def flatten_status_dict(status_dict):
    # type: (Dict[str, Set[Status]]) -> Dict[str, Set[Status]]
    """Take a Dict[str, set[Status]] and flatten its statuses into the text of the statuses.

    Example:

        flatten_status_dict({
            "icecream": [Status, Status],
            "cake": [Status]
            })

            ->

            {"icecream": ["mm icecream", "icecream sucks :("],
            "cake": ["CAKE!!!!"]}

    """
    for term, statuses in status_dict.items():  # Only print the text of the tweet
        status_dict[term] = set([status.text for status in statuses])

    return status_dict


def geobox_from_points(points):
    # type: (list[Point]) -> list[float]
    """Given a list of points, flatten them starting from y and going to x.

    This function exists because for some reason Tweepy/Twitter API likes to
    have a bounding box with flipped lat/long coordinates.

    Example:
        `flatten_points([Point(x=1,y=2), Point(x=2,y=3)])`
        -->
        `[2, 1, 3, 2]`"""
    numbers = []

    for point in points:
        numbers.append(point.y)
        numbers.append(point.x)

    return numbers


def flatten_points(points):
    # type: (list[Point]) -> list[float]
    """Given a list of points, flatten them starting from x and going to y.

    Example:
        `flatten_points([Point(x=1,y=2), Point(x=2,y=3)])`
        -->
        `[1, 2, 2, 3]`"""

    numbers = []

    for point in points:
        numbers.append(point.x)
        numbers.append(point.y)

    return numbers


def geobox_to_geocode(geobox, radius):
    # type: (list[Point, Point], str) -> str
    """Given a geobox and a radius, return a valid Twitter geocode consisting of a point and radius."""
    midpoint = geobox[0].midpoint(geobox[1])

    return "{lat},{lon},{radius}".format(
        lat=midpoint.x,
        lon=midpoint.y,
        radius=radius,
    )


def is_retweet(status):
    # type: (Status) -> bool
    """Tells you if this Status is a retweet."""
    return "RT @" in status.text


def strtobool(v):
    # type: (str) -> bool
    return v.lower() in ["yes", "true", "t", "1"]


def colorama_reset():
    # type: () -> None
    print colorama.Fore.WHITE,
    print colorama.Back.BLACK,


def colorama_highlight_red(text, keyword=None):
    # type: (str, str) -> str
    """
    Highlights text red for a terminal.
    :param text: Text.
    :param keyword: Keyword to highlight.
    :return: Highlighted text.
    """

    if keyword is None:
        keyword = text

    return text.replace(keyword, (colorama.Fore.WHITE + colorama.Back.RED +
                                  keyword +
                                  colorama.Fore.WHITE + colorama.Back.BLACK))
