from TwitterAPI import TwitterAPI
from env import config
import analyze

api = TwitterAPI(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

if __name__ == '__main__':
    max_id = None
    for i in range(5):
        r = api.request('search/tweets', {
            'q': 'メルカリ',
            'lang': 'ja',
            'count': 100,
            'max_id': max_id
        })
        for item in r:
            print(analyze.morph(item['text']))
            max_id = item['id_str']
