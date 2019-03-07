from twitter import TwitterAuthentication
import tweepy
import os


class Scraper():

    def __init__(self, twitter_authentication=None):
        # type: (Scraper, TwitterAuthentication) -> None

        # They did not pass in any authentication. Attempt to auto-detect it.
        if not twitter_authentication:

            print("WARNING: {} object was initialized without any {} object. This is inadvisable.".format(
                self.__class__.__name__,
                TwitterAuthentication.__name__))

            auth_filename = "secrets.json"
            auth_filepath = os.path.abspath(os.path.expanduser(os.path.join("~", auth_filename)))

            # Path to auth file does not exist.
            if not os.path.isfile(auth_filepath):
                print("Auto-detection of {} failed. Searched this path for {}:".format(auth_filename, auth_filename))
                print(auth_filepath)

                print("Either initialize {} with a {} object, or make the file located at the above path.".format(
                    self.__class__.__name__, TwitterAuthentication.__name__))

                raise ValueError("No {} object in initializer".format(TwitterAuthentication.__name__))
            else: # Path to auth file exists.
                self.twitter_authentication = TwitterAuthentication.from_json(auth_filepath)

        else: # They passed us a TwitterAuthentication object
            self.twitter_authentication = twitter_authentication

        # Tweepy API object. Can make API calls.
        self.api = tweepy.API(self.twitter_authentication.oauth_handler,
                              wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        # Default amount of tweets to retrieve.
        self.default_count = 10

    def scrape_terms(self, terms, count=None, geocode=None):
        # type: (Scraper, set[str], int, str) -> dict[str, set[Status]]
        """
        Term-scraping method. Can scrape a set of terms.

        A term is either a hashtag or a piece of text.

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

    def scrape_accounts(self, accounts, count=None):
        # type: (Scraper, set[str], int) -> Dict[str, set[Status]]
        """
        Account-scraping method. Can scrape a set of accounts.

        An account is either a screenname or @screenname, i.e. both 'Dude123' and '@Dude123' are valid.

        :param accounts: List of accounts to search in.
        :param count: Maximum tweets to return per account.
        :return: A dictionary containing {'@Dude123': set[Status]} pairs.
        """
        return {
            "@unfinished_dude": {"I am not implemented!", "Hooray! Unfinished!"},
            "@unfinished_dude2": {"Still not done!"},
        }

    def scrape(self, terms=None, accounts=None, count=None, geocode=None):
        # type: (Scraper, set[str], set[str], int, str) -> dict[str, set[Status]]
        """
        General-purpose scraping method. Can scrape search terms, and accounts.

        :param geocode: Geographical area to search in. Can be blank.
        :param terms:  List of terms to search for.
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

        if (not terms) and (not accounts):
            raise ValueError("No terms or accounts specified.")

        return {
            "hi": {"cool_tweet", "cooler_tweet"}
        }
