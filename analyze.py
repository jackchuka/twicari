import MeCab


def separate_texts(text):
    tagger = MeCab.Tagger('-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    return tagger.parse(text)


def morph(text, option='名詞'):
    tagger = MeCab.Tagger('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    node = tagger.parseToNode(text)
    while node:
        if node.feature.startswith(option):
            try:
                return node.surface
            except UnicodeDecodeError:
                return ''
        node = node.next
