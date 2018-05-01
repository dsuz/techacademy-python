import requests
from bs4 import BeautifulSoup

# 東洋経済オンラインの鉄道最前線ページから特定のキーワードをタイトルに含む記事を抽出するプログラム

topUrl = 'https://toyokeizai.net'   # 抽出を行うサイト
pageUrl =  topUrl + '/list/genre/tetsudosaizensen'  # 抽出を行うページ
useKeyword = True  # キーワードによる記事の抽出を行うか
keywordList = ['東海', 'トヨタ', '名古屋', '愛知']  # 記事を抽出する時のキーワード
line = '-' * 80 # 記事を区切る線

res = requests.get(pageUrl) # ページを読む
soup = BeautifulSoup(res.content, 'html.parser')    # 抽出するために加工する（パースする）

for a in soup.find_all('a'):    # リンクを全部抽出する
    linkUrl = a.get('href')
    if (linkUrl.startswith('/articles')):   # 記事へのリンクは相対URLが /article で始まるので、それを抽出する
        linkTitle = a.text.strip()  # 記事タイトルを取得する。余計なスペースは取り除いておく
        if (useKeyword):    # キーワードによる抽出を行う場合
            if any(keyword in linkTitle for keyword in keywordList):    # キーワードリストに含まれる文字がタイトルに含まれたらそれらを出力する
                print(linkTitle, topUrl + linkUrl)
                print(line)
        else:   # キーワードによる抽出を行わない場合は、普通に全ての記事タイトル・URL を出力する
            print(linkTitle, topUrl + linkUrl)
            print(line)


