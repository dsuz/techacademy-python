import string
import random

def generate_password(length_of_password):
    """パスワードを生成する。パラメータはパスワードの長さ"""
    string_list = string.printable  # パスワードに使う文字。この中にはスペースなどパスワードに使うには不適切な文字も含まれているが、今回は無視する。
    password = ''

    for i in range(length_of_password):
        index = random.randint(0, len(string_list) - 1)
        password = password + string_list[index]

    return password

print('Password generator. How long should your password be?')
buf = input('>>> ')

try:
    password_length = int(buf)
    print(generate_password(password_length))
except ValueError:
    print('invalid value.')
