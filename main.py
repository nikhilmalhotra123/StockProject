from tweets import Tweets
from stockdata import StockData

# TODO: Implement universal logger



def main():
    tweets = Tweets()
    tweets.authentication()
    tweets.getTweetsBySearch("Microsoft", 10)
    stockdata = StockData()
    print(stockdata.getHistoricalDataByID('MSFT', "2018-01-01", "2018-02-02"))

main()
