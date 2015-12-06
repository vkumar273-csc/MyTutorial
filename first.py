__author__ = 'vkumar273'

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

access_token = "109838874-jxnKLamSU9QIDXCVUaglmoDcPuemtc7B7lJxNPPz"
access_secret = "nGVVm4z7hKjRZo9LSW7lcVkuq1MNAs70k00J9XrrchHLW"
consumer_key = "KGgCKoPXY4hLbPd9BHjmD7lWW"
consumer_secret = "DaRe9YWgIzoz1lymTyR5BOjwC4rEqwQhkkm4ofYUtHpbnXp6HH"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def timeline_print():
    for status in tweepy.Cursor(api.home_timeline).items(10):
        # Process a single status
        print(status.text)

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])