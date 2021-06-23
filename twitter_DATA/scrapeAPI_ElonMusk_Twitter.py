import tweepy, sys, pprint, pprint, time
from tweepy import api, Cursor
from decouple import config
import pandas as pd
import pprint

# autenticazione con eventuali manage dell'errore

def twitter_auth():
    try:
        consumer_key=config('API_KEY')
        consumer_secret=config('API_SECRET')
        access_token=config('ACCESS_TOKEN')
        access_secret=config('ACCESS_TOKEN_SECRET')
    
    except KeyError:
        sys.stderr.write("TWITTER environment variable not set")
        sys.exit(1)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    auth = twitter_auth()
    client = tweepy.API(auth, wait_on_rate_limit=True)
    return client

if __name__ == '__main__':
    tweet_list = []
    client = get_twitter_client()
    for status in tweepy.Cursor(client.user_timeline, id='elonmusk').items(10):
        if status.user.id == 44196397:
        
            print('TO: ' + str(status.in_reply_to_screen_name),'TEXT: ' + str(status.text))
    
            

