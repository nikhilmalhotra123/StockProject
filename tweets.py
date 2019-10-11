import tweepy
import config
import logging

logging.basicConfig(level=logging.WARNING)

class Tweets:
    def __init__(self):
        self.api = None

    def authentication(self):
        # Creating the authentication object
        try:
            auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            auth.set_access_token(config.access_token, config.access_token_secret)
            self.api = tweepy.API(auth)
            logging.info("Successfully authenticated with Twitter")
        except Exception as err:
            logging.error("Failed to authenticate with Twitter", str(err))
            exit(1)

    def getTweetsBySearch(self, search, count):
        query = search
        language = "en"
        results = self.api.search(q=query, lang=language, result_type='recent', count=count)
        for tweet in results:
           print(tweet.text)
