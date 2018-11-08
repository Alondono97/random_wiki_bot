import requests
import json 
import time
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

def tweet(link):
  '''
  publishes tweet with given link
  '''
  tweet_data = {'status': link}
  req = requests.post(url=POST_TWEET_URL, data=tweet_data, auth=oauth)

def tweet_wiki_article():

  wiki_art = requests.get('https://en.wikipedia.org/wiki/special:random')
  tweet(wiki_art.url)

if __name__ == '__main__':  
  
  while True:
    tweet_wiki_article()
    time.sleep(43200) #sleeps for 12 hours
  

      

