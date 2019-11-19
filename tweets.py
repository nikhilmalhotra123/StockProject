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
            #auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
            #auth.set_access_token(config.access_token, config.access_token_secret)
            auth = tweepy.AppAuthHandler(config.consumer_key, config.consumer_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)
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
        return (date[-4:] + '-' + month + '-' + date[8:11])

    def getAllTweetsBySearch(self, search, count):
        # https://bhaskarvk.github.io/2015/01/how-to-use-twitters-search-rest-api-most-effectively./
        query = search
        language = "en"
        sinceID = None
        max_id = -1
        tweetCount = 0
        results = []
        while tweetCount < count:
            try:
                if max_id <= 0:
                    if not sinceID:
                        new_tweets = self.api.search(q=query, lang=language, count=100)
                    else:
                        new_tweets = self.api.search(q=query, lang=language, count=100, since_id=sinceID)
                else:
                    if not sinceID:
                        new_tweets = self.api.search(q=query, lang=language, count=100, max_id=str(max_id - 1))
                    else:
                        new_tweets = self.api.search(q=query, lang=language, count=100, max_id=str(max_id - 1), since_id=sinceID)
                if not new_tweets:
                    logging.info("No more tweets found")
                    break
                for tweet in new_tweets:
                    results.append([tweet.text, self.formatDateFromTweet(tweet._json['created_at'])])
                tweetCount += len(new_tweets)
                max_id = new_tweets[-1].id
            except tweepy.TweepError as err:
                logger.error("Error getting tweets", err)
                break
        return results

    def getAllTweetsTillDate(self, search):
        query = search
        language = "en"
        results = self.api.search(q=query, lang=language, result_type='recent', until='2019-10-09', count=count)

    def useCurl(self):
        endpoint = 'https://api.twitter.com/1.1/tweets/search/fullarchive/stockstats.json'
        bearer = "Bearer" + config.bearer
        headers = {"Authorization": bearer, "Content-Type": "application/json"}
        data = '{"query":"microsoft", "fromDate":"201910080000", "toDate":"201910090000"}'
        response = requests.post(endpoint,data=data,headers=headers).json()
        print(json.dumps(response, indent = 2))
