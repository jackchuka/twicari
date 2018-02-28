# twicari
Twi

## 何ができるのか
最近のツイートかから、「メルカリ」とともに呟かれているホットなワードをとってくる

## どうやったのか
TwitterAPIたたいてTFIDFでがんばった

## 実行結果


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
