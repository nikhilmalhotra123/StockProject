import re

def validDateFormat(date):
    datePattern = "[0-9]{4}-[0-9]{2}-[0-9]{2}"
    if re.fullmatch(datePattern, date) is None:
        return False
    return True

def validInterval(interval):
    intervals = ['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo']
    return interval in intervals

def clean_tweet(tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        geeksforgeeks
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
