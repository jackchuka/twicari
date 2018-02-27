import MeCab


def separate_texts(text):
    tagger = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    return tagger.parse(text)


def morph(text, option='名詞'):
    tagger = MeCab.Tagger()
    node = tagger.parseToNode(text)
    while node:
        if node.feature.startswith(option):
            return node.surface
        node = node.next
