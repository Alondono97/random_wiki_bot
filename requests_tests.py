import requests
import json 
import threading
from requests_oauthlib import OAuth1


POST_TWEET_URL = 'https://api.twitter.com/1.1/statuses/update.json'

CONSUMER_KEY = 'api-key'
CONSUMER_SECRET = 'api-secret-key'
ACCESS_TOKEN = 'access-token'
ACCESS_TOKEN_SECRET = 'secret-access-token'

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
    #print(req.json())
def tweet_wiki_article():
    wiki_art = requests.get('https://en.wikipedia.org/wiki/special:random')
    tweet(wiki_art.url)

if __name__ == '__main__':  
    
  
  timer = threading.Timer(3600.0, tweet_wiki_article)
  timer.start()
  while True:
      pass
      
























    