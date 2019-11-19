import logging
import utils
from textblob import TextBlob
from tweets import Tweets
from stockdata import StockData

logging.basicConfig(level=logging.WARNING)

class Model:
    def __init__(self, tweets):
        self.tweets = tweets
        pass

    def getSentimentRating(self, tweet):
        analysis = TextBlob(utils.clean_tweet(tweet))
        print(analysis.sentiment.polarity)

    def getInputData(self, company):
        tweetData = self.tweets.getAllTweetsBySearch("Microsoft", 10)
