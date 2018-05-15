def is_prime(number):
    """引数が素数であるか判定する。アルゴリズムは「エラトステネスのふるい」"""

    # 自明なケース（2以下の数と偶数）に対してはすぐ結果を返す
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    # 3以上の奇数に対しては判定をする
    t = 3  # t は奇数で 3, 5, 7, 9,... と大きくなる
    while t**2 <= number:
        if number % t == 0:  # 割り切れたらその時点で素数ではない
            return False
        t = t + 2

    # 全ての t で割り切れなかったら、素数である
    return True


def main():
    while True:
        print('input number for prime testing.')
        buf = input('>>> ')

        if len(buf) == 0:
            break

        try:
            input_number = int(buf)
            if is_prime(input_number):
                print(buf + ' is a prime number.')
            else:
                print(buf + ' is NOT a prime number.')
        except ValueError:
            print('invalid value.')


if __name__ == '__main__':
    main()
