import csv
import os
from typing import Dict, List, Set

import tweepy
from pymongo import MongoClient
from tweepy import Status

from database.TweetResult import TweetResult, ERelevancy
from twitter import TwitterAuthentication
from util import merge_status_dict, save_statuses_dict_to_mongodb


class Scraper:
    CSV_DELIMITER = '\t'

    def __init__(self, twitter_authentication=None):
        # type: (Scraper, TwitterAuthentication) -> None

        # They did not pass in any authentication. Attempt to auto-detect it.
        if not twitter_authentication:
            self.twitter_authentication = TwitterAuthentication.autodetect_twitter_auth()
        else:  # They passed us a TwitterAuthentication object
            self.twitter_authentication = twitter_authentication

        # Tweepy API object. Can make API calls.
        self.api = tweepy.API(self.twitter_authentication.oauth_handler,
                              wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        # Default amount of tweets to retrieve.
        self.default_count = 10

        # Default accounts to scrape.
        # self.accounts = accounts in data/TwitterAccounts.yml

    def scrape_terms(self,
                     terms: Set[str],
                     count: int = None,
                     geocode: str = None,
                     include_retweets: bool = True) -> Dict[str, List[TweetResult]]:
        """
        Term-scraping method. Can scrape a set of terms.

        A term is either a hashtag or a piece of text.

        :param geocode: Geographical area to search in. Can be blank.
        :param terms:  List of terms to search for.
        :param count: Maximum tweets to return per search term.
        :param include_retweets: Should retweets be included?
        :return: A dictionary containing {'search-term': List[TweetResult]} pairs.
        """

        if not count:
            count = self.default_count

        results: Dict[str, List[TweetResult]] = {}

        # For each search term,
        for search_term in terms:

            query = search_term

            if not include_retweets:
                query += ' -filter:retweets'
                query += ' -filter:nativeretweets'

            # Make a cursor that can get tweets.
            cursor = tweepy.Cursor(self.api.search, q=query, geocode=geocode, tweet_mode='extended')

            # For each result of a search term,
            for status in cursor.items(count):  # type: Status

                if search_term not in results:
                    results[search_term] = list()

                result = TweetResult(data=status, tags=[search_term], relevancy=ERelevancy.UNCATEGORIZED)

                # Add the status to a particular search term.
                results[search_term].append(result)

        return results

    def scrape_accounts(self,
                        accounts: Set[str],
                        count: int = None) -> Dict[str, List[TweetResult]]:
        """
        Account-scraping method. Can scrape a set of accounts.

        An account is either a screenname or @screenname, i.e. both 'Dude123' and '@Dude123' are valid.

        :param accounts: List of accounts to search in.
        :param count: Maximum tweets to return per account.
        :return: A dictionary containing {'@AccountName': List[TweetResult]} pairs.
        """

        if not count:
            count = self.default_count

        results = dict()

        for account in accounts:
            statuses: List[Status] = self.api.user_timeline(screen_name=account, count=count)

            if account not in results:
                results[account] = list()

            for status in statuses:
                result = TweetResult(data=status, tags=[account], relevancy=ERelevancy.UNCATEGORIZED)

                results[account].append(result)

                return results

    def scrape(self, terms: Set[str] = None,
               accounts: Set[str] = None,
               count: int = None,
               geocode: str = None,
               include_retweets: bool = True) -> Dict[str, List[TweetResult]]:
        """
        General-purpose scraping method. Can scrape search terms, and accounts.

        :param geocode: Geographical area to search in. Can be blank.
        :param terms:  List of terms to search for.
        :param accounts: List of account names to search.
        :param count: Maximum tweets to return per search term.
        :param include_retweets: Should retweets be included?
        :return: A dictionary containing {'search-term': List[Status]} pairs.

        Examples:
            >>> self.scrape(geocode="41.8297855,-87.666775,50mi", terms={"pizza", "waffles"}, count=3)
            {'pizza': {TweetResult, TweetResult, TweetResult},
            'waffles': {TweetResult, TweetResult}}
        """
        if not count:
            count = self.default_count

        if (not terms) and (not accounts):
            raise ValueError("No terms or accounts specified.")

        results = dict()

        if terms:
            terms_results = self.scrape_terms(terms=terms, count=count, geocode=geocode,
                                              include_retweets=include_retweets)

            results = merge_status_dict(results, terms_results)

        if accounts:
            accounts_results = self.scrape_accounts(accounts=accounts, count=count)

            results = merge_status_dict(results, accounts_results)

        return results

    def scrape_and_save(self,
                        terms: Set[str] = None,
                        accounts: Set[str] = None,
                        count: int = None,
                        geocode: str = None,
                        dbname='scraper_tweets'):

        # First, retrieve search results via scrape
        results = self.scrape(terms=terms, accounts=accounts, count=count, geocode=geocode)

        # Establish connection to the host
        client = MongoClient()

        # Access database where the scraped tweets will be saved
        db = client[dbname]

        # Save all tweets to the database
        save_statuses_dict_to_mongodb(results, db)

        return results

    def save_statusdict_to_csv(self,
                               statusdict: Dict[str, List[TweetResult]],
                               filepath: str,
                               overwrite: bool = False,
                               relevant_column: bool = False):
        """Save a status dict to a CSV file.
        :param statusdict A {str: [TweetResult, TweetResult, ...]} dictionary.
        :param filepath A path to the file to output to.
        :param overwrite Should we overwrite `filepath` if it exists?
        :param relevant_column Should we insert an extra column for hand-categorizing in Excel?
        """

        dirname = os.path.dirname(filepath)

        if not os.path.exists(dirname):
            raise NotADirectoryError("Directory {} does not exist!".format(dirname))

        if os.path.isfile(filepath):
            if not overwrite:
                raise FileExistsError("File at '{}' already exists!".format(filepath))

        fieldnames = [
            'category', 'tweet_id', 'text', 'date', 'retweet_count',

            'geo',

            'coordinates',

            'place_id', 'place_centroid', 'place_country', 'place_country_code', 'place_full_name',
            'place_name', 'place_type'
        ]

        if relevant_column:
            fieldnames.append("relevant")

        with open(filepath, 'w', encoding='utf-16', newline='') as file:
            fileWriter = csv.DictWriter(file, delimiter=Scraper.CSV_DELIMITER, quotechar='"', quoting=csv.QUOTE_ALL,
                                        fieldnames=fieldnames)

            fileWriter.writeheader()

            for keyword, statuses in statusdict.items():

                for status in statuses:

                    data = {
                        "category": keyword,
                        "tweet_id": status,
                        "text": status.get_text(),
                        "date": status.data.created_at,
                        'retweet_count': status.data.retweet_count,
                    }

                    if relevant_column:
                        data.update({
                            'relevant': "UNCATEGORIZED"
                        })

                    if status.data.geo:
                        data.update({
                            "geo": ','.join(str(x) for x in status.data.geo['coordinates']),
                        })

                    if status.data.coordinates:
                        data.update({
                            'coordinates': ','.join(str(x) for x in status.data.coordinates['coordinates']),
                        })

                    # If the status has a place, then add its data!
                    if status.data.place:
                        data.update({
                            'place_id': status.data.place.id,
                            # We have to use the API for this one to look it up.
                            'place_centroid': ','.join(str(x) for x in self.api.geo_id(status.data.place.id).centroid),
                            'place_country': status.data.place.country,
                            'place_country_code': status.data.place.country_code,
                            'place_full_name': status.data.place.full_name,
                            'place_name': status.data.place.name,
                            'place_type': status.data.place.place_type,
                        })

                    # Write all the data we've collected so far.
                    fileWriter.writerow(data)

        return filepath
