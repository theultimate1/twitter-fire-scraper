"""
This file demonstrates the Scraper class' ability to scrape small amounts of tweets about a simple term, like 'pizza'.
"""
from pprint import pprint

from scraper import Scraper
from twitter import GEOBOX_CHICAGO
from util import geobox_to_geocode

if __name__ == '__main__':
    scraper = Scraper()

    terms = {"pizza"}

    results = scraper.scrape_terms(terms={"pizza"}, count=3)
    print("{} on all of twitter:".format(", ".join(terms)))
    pprint(results)

    results = scraper.scrape_terms(geocode=geobox_to_geocode(GEOBOX_CHICAGO, "20mi"), terms={"pizza"}, count=3)
    print("{} in chicago:".format(", ".join(terms)))
    pprint(results)
