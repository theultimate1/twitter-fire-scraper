"""
This file demonstrates the Scraper class' ability to scrape small amounts of tweets about a combination of search terms
and hashtags, like 'icecream', '#pizza', and '#steak'.
"""
from pprint import pprint

from scraper import Scraper
from twitter import GEOBOX_CHICAGO
from util import geobox_to_geocode

if __name__ == '__main__':
    terms = {"icecream"}
    hashtags = {"steak", "pizza"}

    scraper = Scraper()

    results = scraper.scrape(terms={"icecream"}, hashtags={"steak", "pizza"}, count=3)
    print("{} and {} on all of twitter:".format(
        ", ".join(terms),
        ", ".join(hashtags)
    ))
    pprint(results)

    results = scraper.scrape(terms={"icecream"}, hashtags={"steak", "pizza"},
                             geocode=geobox_to_geocode(GEOBOX_CHICAGO, "20mi"), count=3)
    print("{} and {} in chicago:".format(
        ", ".join(terms),
        ", ".join(hashtags)
    ))
    pprint(results)
