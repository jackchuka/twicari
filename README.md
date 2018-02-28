# twicari

## 何ができるのか
最近のツイートかから、「メルカリ」とともに呟かれているホットなワードをとってくる

## どうやったのか
TwitterAPIたたいてTFIDFで重要そうな単語を引っ張ってきた

## 何に使えるのか
今お客様はこんなことを考えている、こんなことで困っているというのがすぐにわかるようになる。⇨アクティブサポート！！

また、メルカリがどんなことで話題にされているかもわかるようになる


## 実行結果
```json
{"freq": 1.0, "word": "京都"},
{"freq": 1.0, "word": "初任給"},
{"freq": 0.7675369941803794, "word": "ねむの木"},
{"freq": 0.3837684970901897, "word": "洛北"},
{"freq": 0.3837684970901897, "word": "ｋｙｏｔｏｎｅｍｕｎｏｋｉ"}
```
例えば「京都」だとこのようなツイートがホットになっています

<img width="400" alt="2018-02-28 18 26 04" src="https://user-images.githubusercontent.com/15362961/36780003-23e67830-1cb5-11e8-8dc3-eed4baa70d08.png">


## Setup on MacOS

### Clone Repo
```bash
git clone https://github.com/jackchuka/twicari.git
git submodule update --init --recursive
```

### install dependencies
```bash
brew install mecab
brew install mecab-ipadic
brew install pip
```

### install python dependencies
```bash
pip install -r requirements.txt
## install neologd dictionary
./neologd/bin/install-mecab-ipadic-neologd 
```

## Run
```bash
python main.py
```
