from twitter import TwitterAuthentication
import tweepy


# noinspection PyUnresolvedReferences
class Scraper():

    def __init__(self):

        # Twitter authentication object.
        self.twitter_authentication = TwitterAuthentication()

        # Tweepy API object. Can make API calls.
        self.api = tweepy.API(self.twitter_authentication.oauth_handler,
                              wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        # Default amount of tweets to retrieve.
        self.default_count = 10

    def scrape_terms(self, terms, geocode=None, count=None):
        # type: (Scraper, set[str], str, int) -> dict[str, set[Status]]
        """
        Term-scraping method. Can scrape a set of terms.

        :param geocode: Geographical area to search in. Can be blank.
        :param terms:  List of terms to search for.
        :param count: Maximum tweets to return per search term.
        :return: A dictionary containing {'search-term': set[Status]} pairs.
        """

        if not count:
            count = self.default_count

        results = {}  # type: dict[str, set[Status]]

        # For each search term,
        for search_term in terms:

            # Make a cursor that can get tweets.
            cursor = tweepy.Cursor(self.api.search, q=search_term, geocode=geocode)

            # For each result of a search term,
            for status in cursor.items(count):  # type: Status

                if search_term not in results:
                    results[search_term] = set()

                # Add the status to a particular search term.
                results[search_term].add(status)

        return results

    def scrape(self, geocode=None, terms=None, hashtags=None, accounts=None, count=None):
        # type: (Scraper, str, set[str], set[str], set[str], int) -> dict[str, set[Status]]
        """
        General-purpose scraping method. Can scrape terms, hashtags, and accounts.

        :param geocode: Geographical area to search in. Can be blank.
        :param terms:  List of terms to search for.
        :param hashtags: List of hashtags to search.
        :param accounts: List of account names to search.
        :param count: Maximum tweets to return per search term.
        :return: A dictionary containing {'search-term': set[Status]} pairs.

        Examples:
            >>> scrape(geocode="41.8297855,-87.666775,50mi", terms={"pizza", "waffles"}, maximum=3)
            {'pizza': {Status, Status, Status},
            'waffles': {Status, Status}}
        """
        if not count:
            count = self.default_count

        if (not terms) and (not hashtags) and (not accounts):
            raise ValueError("No terms, hashtags, or accounts specified.")

        return {
            "hi": {"cool_tweet", "cooler_tweet"}
        }
