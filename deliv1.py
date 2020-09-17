from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import os

consumer_key=os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"]
access_token=os.environ["TWITTER_ACCEESS_TOKEN"]
access_token_secret=os.environ["TWITTER_SECRET_TOKEN"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

account_list = []
if (len(sys.argv) > 1):
  account_list = sys.argv[1:]
else:
  print("Please provide a list of usernames at the command line.")
  sys.exit(0)
  
if len(account_list) > 0:
  for target in account_list:
    
    for status in Cursor(auth_api.user_timeline, id=target).items():
      print(status.text + "\n")
