from TwitterAPI import TwitterAPI
from env import config

api = TwitterAPI(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

if __name__ == '__main__':
    r = api.request('search/tweets', {'q': 'mercari', 'count': 100})
    for item in r:
        print(item['text'])
