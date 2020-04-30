import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# メールアドレスとパスワードの指定
USER = "fufu.engineer1237@gmail.com"
PASS = "Egawa1237"

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "userId":USER,
    "userPass":PASS,
    # "back":"index.php",
    # "mml_id":"0"
}

# action
url_login = "https://member.accesstrade.net/atv3/login.html"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

# マイページのURLをピックアップする
soup = BeautifulSoup(res.text,"html.parser")
a = soup.select_one(".islogin a")# isloginクラス要素内のaタグ
if a is None:
    print("マイページが取得できませんでした")
    quit()

# 相対URLを絶対URLに変換
url_mypage = urljoin(url_login, a.attrs["href"])
print("マイページ=", url_mypage)