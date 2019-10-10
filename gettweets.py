import tweepy
import config
import logging

logging.basicConfig(level=logging.WARNING)

class Tweet:
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

    def getTweetsBySearch(self, search, count):
        # The search term you want to find
        query = search
        # Language code (follows ISO 639-1 standards)
        language = "en"
        # Calling the user_timeline function with our parameters
        results = self.api.search(q=query, lang=language, result_type='recent', count=count)
        # foreach through all tweets pulled
        for tweet in results:
           # printing the text stored inside the tweet object
           print(tweet.text)
