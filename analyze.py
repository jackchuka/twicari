import MeCab
import numpy as np
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
