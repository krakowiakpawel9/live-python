from tweetlib import tweetlib


ts = tweetlib.TweetLib(username='e_smartdataorg', max_tweets=2)
tweets = ts.get_tweets()

for tweet in tweets:
    print(tweet['text'])
