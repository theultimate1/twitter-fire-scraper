import colorama
from tweepy import Status
from typing import Union

from models import Point


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
