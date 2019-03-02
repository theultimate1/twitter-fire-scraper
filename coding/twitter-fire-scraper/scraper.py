from twitter import TwitterAuthentication


# noinspection PyUnresolvedReferences
class Scraper():

    def __init__(self):
        self.twitter_authentication = TwitterAuthentication()

    def scrape(self, geocode, terms, hashtags, accounts, count=10):
        # type: (Scraper, str, set[str], set[str], set[str], int) -> dict[str, set[Status]]
        """
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

        if (not terms) and (not hashtags) and (not accounts):
            raise ValueError("No terms, hashtags, or accounts specified.")

        return {
            "hi": {"cool_tweet", "cooler_tweet"}
        }
