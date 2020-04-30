import pandas as pd # pandasのインポート
from bs4 import BeautifulSoup # BeautifulSoupのインポート
import requests # requestsのインポート
# from google.colab import files

url = "https://www.ryukke.com/"

# TODO1 requestsで、指定されたURLのHTMLを取得してください。
response = requests.get(url).text
# print(response)

soup = BeautifulSoup(response, 'html.parser') # BeautifulSoupの初期化
# print(soup.prettify())

#TODO3 h3を複数取得してください。
tags = soup.find_all("div", {"class":"post-title"})
for tag in tags:
    print(tag.a.get('title'))
    print(tag.a.get('href'))

# データフレームを作成してください。列名は、name, urlです。
# columns = ["name", "url"]
# df2 = pd.DataFrame(columns=columns)

# # 記事名と記事URLをデータフレームに追加してください
# for tag in tags:
#  name = tag.a.string
#  url = tag.a.get("href")
#  se = pd.Series([name, url], columns)
#  print(se)
#  df2 = df2.append(se, columns)

# # result.csvという名前でCSVに出力してください。
# filename = "ryuuken_blog_new_title.csv"
# df2.to_csv(filename, encoding = 'utf-8-sig') #encoding指定しないと、エラーが起こります。おまじないだともって入力します。
# files.download(filename)