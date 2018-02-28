from TwitterAPI import TwitterAPI
from env import config
import analyze

api = TwitterAPI(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

if __name__ == '__main__':
    max_id = None
    tweets = []
    pnmean_list = []
    text_list = []
    count = 0
    last_created = None

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
            count += 1
            tweet_text = item['text']
            text_list.append(tweet_text)
            max_id = item['id_str']
            last_created = item['created_at']
        morphed = analyze.morph(' '.join(str(x) for x in text_list))
        tweets.append(morphed)
    analyze.vectorize(tweets)
