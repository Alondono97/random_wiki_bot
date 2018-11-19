import requests
import json 
import time
import wikipedia
from requests_oauthlib import OAuth1


POST_TWEET_URL = 'https://api.twitter.com/1.1/statuses/update.json'

#reads api keys from text file
f = open('twitter_api_keys.txt')
keys = f.readlines()

#strips new line character from api key
for i in range(4):
  keys[i] = keys[i].strip() 

CONSUMER_KEY = keys[0]
CONSUMER_SECRET = keys[1]
ACCESS_TOKEN = keys[2]
ACCESS_TOKEN_SECRET = keys[3]

oauth = OAuth1(CONSUMER_KEY,
  client_secret=CONSUMER_SECRET,
  resource_owner_key=ACCESS_TOKEN,
  resource_owner_secret=ACCESS_TOKEN_SECRET)

def tweet(post):
  
  #publishes tweet with given link
  
  tweet_data = {'status': post}
  req = requests.post(url=POST_TWEET_URL, data=tweet_data, auth=oauth)

def tweet_wiki_article():
  
  #requests random wiki page
  rand_article = wikipedia.random(1)
  
  #get wiki page
  wiki_page = wikipedia.page(rand_article)
  #page article summary
  wiki_summary = wikipedia.summary(rand_article)
  #keep the summary within twitter char limit
  if len(wiki_summary) > 280:
    wiki_summary = wiki_summary[0:280]

  #page url
  wiki_url = wiki_page.url 

  tweet(rand_article + ': ' + wiki_url)
  print('test') #it wouldn't execute both the summary tweet and the link tweet without this
  tweet(wiki_summary)
  
  
  
if __name__ == '__main__':  
  
  while True:
    tweet_wiki_article()
    time.sleep(43200) #sleeps for 12 hours
  

      

