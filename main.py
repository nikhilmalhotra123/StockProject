from tweets import Tweets
from stockdata import StockData
from model import Model

# TODO: Implement universal logger



def main():
    tweets = Tweets()
    tweets.authentication()
    #tweets.getAllTweetsBySearch("Microsoft", 200)
    stockdata = StockData()
    #print(stockdata.getHistoricalDataByID('MSFT', "2018-01-01", "2018-02-02"))
    model = Model(tweets)
    model.getInputData('MSFT')

main()
