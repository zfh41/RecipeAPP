import os
import flask
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import random

app = flask.Flask(__name__)

consumer_key=os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"]
access_token=os.environ["TWITTER_ACCEESS_TOKEN"]
access_token_secret=os.environ["TWITTER_SECRET_TOKEN"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)



@app.route('/')

def index():
    food_list = ["fried chicken", "ice cream", "salad", "lollipop", "mochi", "popcorn", "eggs"]
    tweetList=[]
    userList=[]
    dateList=[]
    randNum = random.randrange(0, 7)
    end_date = datetime.utcnow() - timedelta(days=30)
    tweets = Cursor(auth_api.search, q = food_list[randNum], lang="en").items(1)
      
    for status in tweets:
        tweetList.append(status.text)
        userList.append(status.user.screen_name)
        dateList.append(status.created_at.strftime('%m/%d/%Y, %H:%M:%S'))
    
        if status.created_at < end_date:
            break
      
    return flask.render_template("index.html", len = len(tweetList), tweetList = tweetList, userList=userList, dateList=dateList)

# if __name__ == "__main__":
app.run(
port=int(os.getenv('PORT', 8080)), host=os.getenv('IP','0.0.0.0'))