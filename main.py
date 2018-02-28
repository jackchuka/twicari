from TwitterAPI import TwitterAPI
from env import config
import analyze

api = TwitterAPI(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

if __name__ == '__main__':
    max_id = None
    document = []
    pnmean_list = []
    text_list = []

    for i in range(1):
        r = api.request('search/tweets', {
            'q': 'メルカリ',
            'lang': 'ja',
            'count': 100,
            'max_id': max_id
        })
        for item in r:
            text_list.append(item['text'])
            pnmean_list.append(analyze.get_pnmean(analyze.add_pnvalue(analyze.get_diclist(item['text']))))
            document.append(analyze.morph(item['text']))
            max_id = item['id_str']
    analyze.vectorize(document)
