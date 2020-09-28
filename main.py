import os
import flask
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import random
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json

app = flask.Flask(__name__)

dotenv_path = join(dirname(__file__), 'twitter.env')
load_dotenv(dotenv_path)

spoonacular_key = os.environ['SPOONACULAR_KEY']
consumer_key=os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"]
access_token=os.environ["TWITTER_ACCEESS_TOKEN"]
access_token_secret=os.environ["TWITTER_SECRET_TOKEN"]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)



@app.route('/')

def index():
    food_list = ["fried chicken", "ice cream", "salad", "butter", "chocolate", "popcorn", "eggs", "yogurt", "fish"]
    
    tweetList=[]
    userList=[]
    dateList=[]
    
    ingredientList=[]
    randNum = random.randrange(0, 9)
    end_date = datetime.utcnow() - timedelta(days=30)
    q = food_list[randNum]
    
    url = "https://api.spoonacular.com/recipes/findByIngredients?ingredients={}&apiKey={}".format(q, spoonacular_key)
   
    
    tweets = Cursor(auth_api.search, q, tweet_mode="extended", lang="en").items(1)
    
    response = requests.get(url)
    json_body = response.json()
    
    jsonLength=len(json_body)
    
    randN=random.randrange(0, jsonLength)
    
    ident=str(json.dumps(json_body[randN]["id"], indent=2))
    
    newURL="https://api.spoonacular.com/recipes/{}/information?includeNutrition=false&apiKey={}".format(ident, spoonacular_key)
    
    response = requests.get(newURL)
    json_body = response.json()
        
    
    title=json.dumps(json_body["title"], indent=2)
    title=title.strip("\"")
    print(json.dumps(json_body["image"]))
    imageURL=json.dumps(json_body["image"]).strip("\"")
    servings=json.dumps(json_body["servings"])
    prepTime=json.dumps(json_body["readyInMinutes"])
    spoonURL=json.dumps(json_body["sourceUrl"])
    
    for i in json_body["extendedIngredients"]:
        ingredientList.append(i["original"])
    
      
    for status in tweets:
        try:
            tweetList.append(status.retweeted_status.full_text)
        except AttributeError:  # Not a Retweet
            tweetList.append(status.full_text)
        userList.append(status.user.screen_name)
        dateList.append(status.created_at.strftime('%m/%d/%Y, %H:%M:%S'))
    
        if status.created_at < end_date:
            break
      
    return flask.render_template("index.html", len = len(ingredientList), tweetList = tweetList, userList=userList, \
    ingredientList=ingredientList, dateList=dateList, servings=servings, prepTime=prepTime, title=title,imageURL=imageURL, spoonURL=spoonURL)

# if __name__ == "__main__":
app.run(
port=int(os.getenv('PORT', 8080)), host=os.getenv('IP','0.0.0.0'))