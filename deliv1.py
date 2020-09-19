import os
import flask
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys

app = flask.Flask(__name__)

consumer_key=os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"]
access_token=os.environ["TWITTER_ACCEESS_TOKEN"]
access_token_secret=os.environ["TWITTER_SECRET_TOKEN"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

food_list = ["fried chicken", "ice cream", "salad", "lollipop", "mochi", "popcorn", "eggs"]
  
<<<<<<< HEAD
if len(food_list) > 0:
  for target in food_list:
    end_date = datetime.utcnow() - timedelta(days=30)
    tweets = Cursor(auth_api.search, q = target, lang="en").items(5)
    tweetList=[]
    userList=[]
    dateList=[]
    
    
    for status in tweets:
      tweetList.append(status.text)
      userList.append(status.user.screen_name)
      dateList.append(str(status.created_at))
      print("Tweet: " + status.text + " User: " + status.user.screen_name + " datecreated: " + str(status.created_at) + "\n")
      if status.created_at < end_date:
          break

@app.route('/')
def hello():
    return flask.render_template("index.html", len = len(tweetList), tweetList = tweetList, userList=userList, dateList=dateList)


if __name__ == "__main__":
    app.run(
    port=int(os.getenv('PORT', 8080)), host=os.getenv('IP','0.0.0.0'))
=======
if len(account_list) > 0:
  for target in account_list:
    
    for status in Cursor(auth_api.user_timeline, id=target).items():
      print(status.text + "\n")
>>>>>>> b33132831cde14bcb35135a45539c3f6c64557ae
