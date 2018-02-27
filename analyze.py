import MeCab


def separate_texts(text):
    tagger = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    return tagger.parse(text)


def morph(text):
    tagger = MeCab.Tagger()
    return tagger.parse(text)
