import MeCab
import re
import numpy as np
import pandas as pd
from statistics import mean
from sklearn.feature_extraction.text import TfidfVectorizer


def separate_texts(text):
    tagger = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    return tagger.parse(text)


def morph(sentence, option='固有名詞'):
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    node = tagger.parseToNode(sentence)
    option_vars = []
    while node:
        if option in node.feature:
            try:
                text = node.surface
                if not is_exclude_word(text):
                    option_vars.append(text)
            except UnicodeDecodeError:
                pass
        node = node.next
    return ' '.join(str(x) for x in option_vars)


exclude_words = [
    'メルカリ',
    'メルカリアッテ',
    'mercari',
    'フリマ',
    'フリマアプリ',
    'リプ',
    'RT',
    '拡散',
]


def is_exclude_word(text):
    if len(text) <= 1:
        return True
    if isalnum(text):
        return True
    for word in exclude_words:
        if word == text:
            return True
    return False


def isalnum(s):
    alnumReg = re.compile(r'^[a-zA-Z0-9]+$')
    return alnumReg.match(s) is not None


def vectorize(tweets):
    np.set_printoptions()
    tweets = np.array(tweets)

    vectorizer = TfidfVectorizer(min_df=3)

    vecs = vectorizer.fit_transform(tweets)
    word_vector = vectorizer.get_feature_names()

    dct_list = []
    for vec in vecs.toarray():
        for index, freq in enumerate(vec):
            if freq > 0:
                dct = dict([('freq', freq), ('word', word_vector[index])])
                dct_list.append(dct)

    sorted_list = [dict(t) for t in set([tuple(d.items()) for d in dct_list])]
    sorted_list = sorted(sorted_list, key=lambda k: k['freq'])

    print(sorted_list)


def get_diclist(text):
    tagger = MeCab.Tagger()
    parsed = tagger.parse(text)  # 形態素解析結果（改行を含む文字列として得られる）
    lines = parsed.split('\n')  # 解析結果を1行（1語）ごとに分けてリストにする
    lines = lines[0:-2]  # 後ろ2行は不要なので削除
    diclist = []
    for word in lines:
        l = re.split('\t|,', word)  # 各行はタブとカンマで区切られてるので
        d = {'Surface': l[0], 'POS1': l[1], 'POS2': l[2], 'BaseForm': l[7]}
        diclist.append(d)
    return diclist


def add_pnvalue(diclist_old):
    pn_df = pd.read_csv(
        'dictionary/pn_ja.dic.txt',
        sep=':',
        encoding='Shift-JIS',
        names=('Word', 'Reading', 'POS', 'PN'),
    )
    word_list = list(pn_df['Word'])
    pn_list = list(pn_df['PN'])  # 中身の型はnumpy.float64
    pn_dict = dict(zip(word_list, pn_list))

    diclist_new = []
    for word in diclist_old:
        base = word['BaseForm']
        if base in pn_dict:
            pn = float(pn_dict[base])
        else:
            pn = 'notfound'
        word['PN'] = pn
        diclist_new.append(word)
    return diclist_new


def get_pnmean(diclist):
    pn_list = []
    for word in diclist:
        pn = word['PN']
        if pn != 'notfound':
            pn_list.append(pn)  # notfoundだった場合は追加もしない
    if len(pn_list) > 0:  # 「全部notfound」じゃなければ
        pnmean = mean(pn_list)
    else:
        pnmean = 0  # 全部notfoundならゼロにする
    return (pnmean)
