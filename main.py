from TwitterAPI import TwitterAPI
from env import config
import analyze

api = TwitterAPI(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

if __name__ == '__main__':
    max_id = None
    tweets = []
    pnmean_list = []
    text_list = []

    for i in range(2):
        r = api.request('search/tweets', {
            'q': 'メルカリ -"item.mercari" -"招待コード"',
            'lang': 'ja',
            'count': 100,
            'max_id': max_id
        })
        for index, item in enumerate(r):
            # text_list.append(item['text'])
            # pnmean_list.append(analyze.get_pnmean(analyze.add_pnvalue(analyze.get_diclist(item['text']))))
            tweet_text = item['text']

            morphed = analyze.morph(tweet_text)
            tweets.append(morphed)
            max_id = item['id_str']
    analyze.vectorize(tweets)
