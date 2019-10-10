from gettweets import GetTweet

# TODO: Implement universal logger
def main():
    tweet = Tweet()
    tweet.authentication()
    tweet.getTweetsBySearch("Microsoft", 5)

main()
