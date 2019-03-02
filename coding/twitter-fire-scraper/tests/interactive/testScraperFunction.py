from pprint import pprint

from scraper import Scraper
from twitter import GEOBOX_CHICAGO
from util import geobox_to_geocode

if __name__ == '__main__':
    scraper = Scraper()

    results = scraper.scrape(geocode=geobox_to_geocode(GEOBOX_CHICAGO, "20mi"), terms="pizza")

    print("Pizza!")
    pprint(results)
