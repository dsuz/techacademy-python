import httplib2, os
from apiclient import discovery
import gmail_auth
import base64
import email

"""
使い方:

    変数 keywords（抽出するキーワード）を書き換えて実行する

注意:

    gmail_auth.py が必要

参考にしたページ:

    PythonでGmailのメールを確認しよう
    https://news.mynavi.jp/article/zeropython-22/
    
    PythonでGmailを確認しよう その2
    https://news.mynavi.jp/article/zeropython-23/
"""

keywords = ['無料', '関西', 'セール', 'お得']   # メール本文から抽出するキーワード
how_many_mails_to_be_got = 50   # 検索対象のメール数
display_range = 30  # キーワードの前後、何文字を抽出して表示するか


# Gmailのサービスを取得
def gmail_get_service():
    # ユーザー認証の取得
    credentials = gmail_auth.gmail_user_auth()
    http = credentials.authorize(httplib2.Http())
    # GmailのAPIを利用する
    service = discovery.build('gmail', 'v1', http=http)
    return service


# メッセージの一覧を取得
def gmail_get_messages():
    service = gmail_get_service()
    # メッセージの一覧を取得
    messages = service.users().messages()
    msg_list = messages.list(userId='me', maxResults=how_many_mails_to_be_got).execute()

    for msg in msg_list['messages']:
        topid = msg['id']
        data = messages.get(userId='me', id=topid, format='raw').execute()
        # メッセージの本文を取り出す
        raw_data = base64.urlsafe_b64decode(data['raw'])
        eml = email.message_from_bytes(raw_data)
        body = ""   # body = 本文
        for part in eml.walk():
            if part.get_content_type() != 'text/plain':
                continue
            s = part.get_payload(decode=True)
            if isinstance(s, bytes):
                charset = part.get_content_charset() or 'iso-2022-jp'
                s = s.decode(str(charset), errors="replace")
            body += s
        filter_text(body, keywords, display_range) # 本文からキーワード前後の文字を抽出して出力する


def filter_text(text, keyword_list, range):
    """ 与えられた text から keyword_list に含まれたキーワードの前後 range を抽出し、出力する """
    for keyword in keyword_list:
        index = text.find(keyword)
        if index > -1:
            print('■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■')
            print('[', keyword, ']:', text[index - range : index + range])


# メッセージの取得を実行
gmail_get_messages()
