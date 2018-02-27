import MeCab

def seperate_texts(text):
    tagger = MeCab.Tagger("-Owakati")
    return tagger.parse(text)

def morph(text):
    tagger = MeCab.Tagger()
    return tagger.parse(text)
