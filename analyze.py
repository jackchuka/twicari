import MeCab
import re
import numpy as np
import pandas as pd
from statistics import mean
from sklearn.feature_extraction.text import TfidfVectorizer


def separate_texts(text):
    tagger = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    return tagger.parse(text)


def morph(sentence, option='名詞'):
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    node = tagger.parseToNode(sentence)
    option_vars = []
    while node:
        if node.feature.startswith(option):
            try:
                option_vars.append(node.surface)
            except UnicodeDecodeError:
                pass
        node = node.next
    tagger = MeCab.Tagger('-Owakati')
    return tagger.parse(' '.join(str(x) for x in option_vars))


def vectorize(document):
    np.set_printoptions()
    docs = np.array(document)

    vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u'(?u)\\b\\w+\\b')

    vecs = vectorizer.fit_transform(docs)
    print(vecs.toarray())

    word_vector = vectorizer.get_feature_names()

    for vec in vecs.toarray():
        for index, freq in enumerate(vec):
            if freq > 0:
                print(freq, word_vector[index])


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
        names=('Word', 'Reading', 'POS', 'PN')
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
