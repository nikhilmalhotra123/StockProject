import logging
import time
import utils
import yfinance as yf

logging.basicConfig(level=logging.WARNING)

class StockData:
    def __init__(self):
        print("init")

    """
    startdate and enddate are in the form "YYY-MM-DD"
    data is a pandas dataframe
    """
    def getHistoricalDataByID(self, id, startdate, enddate, interval="1d"):
        # TODO: put input checks in everywhere
        # TODO: Check for valid stock id
        if not utils.validDateFormat(startdate):
            logging.error("Invalid start date format. Received %s. Wanted YYYY-MM-DD", startdate)
            exit(1)
        if not utils.validDateFormat(enddate):
            logging.error("Invalid end date format. Received %s. Wanted YYYY-MM-DD", enddate)
            exit(1)
        try:
            data = yf.download(id, startdate, enddate, interval=interval) # Data is a pandas dataframe
        except Exception as err:
            logging.error("Failed to get historical data", str(err))
            exit(1)

        return data

    def getAllHistoricalDataByID(self, id):
        try:
            data = yf.download(id, period='max') # Data is a pandas dataframe
        except Exception as err:
            logging.error("Failed to get all historical data", str(err))
            exit(1)

        return data

    def getLivePriceByID(self, id):
        # TODO: Check for valid stock id
        stock = yf.Ticker(id)
        return stock.info['regularMarketPrice']
