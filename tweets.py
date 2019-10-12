import tweepy
import config
import logging
import requests
import json
import calendar

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

    def formatDateFromTweet(self, date):
        month = ''
        try:
            month = str(list(calendar.month_abbr).index(date[4:7]))
        except Exception as err:
            logging.error("Failed to convert month to number")
            exit(1)
        if len(month) == 1:
            month = '0' + month
        if len(month) != 2:
            logging.error("Failed to get correct month")
            exit(1)
        print(date[-4:] + '-' + month + '-' + date[8:11])

    def getTweetsBySearch(self, search, count):
        query = search
        language = "en"
        results = self.api.search(q=query, lang=language, result_type='recent', until='2019-10-09', count=count)
        for tweet in results:
            self.formatDateFromTweet(tweet._json['created_at'])

    def useCurl(self):
        endpoint = 'https://api.twitter.com/1.1/tweets/search/fullarchive/stockstats.json'
        bearer = "Bearer" + config.bearer
        headers = {"Authorization": bearer, "Content-Type": "application/json"}
        data = '{"query":"microsoft", "fromDate":"201910080000", "toDate":"201910090000"}'
        response = requests.post(endpoint,data=data,headers=headers).json()
        print(json.dumps(response, indent = 2))
