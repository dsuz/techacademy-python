def is_prime(number):
    """引数が素数であるか判定する。アルゴリズムは「エラトステネスのふるい」"""
    if number < 2: return False
    elif number == 2 : return True
    elif number % 2 == 0: return False

    for i in range(3, round(number / 2), 2):
        if number % i == 0:
            return False

    return True

def main():
    while True:
        print ('input number for prime testing.')
        buf = input('>>> ')

        if len(buf) == 0: break
    
        try:
            input_number = int(buf)
            if is_prime(input_number): print(buf + ' is a prime number.')
            else: print(buf + ' is NOT a prime number.')
        except ValueError:
            print('invalid value.')

if __name__ == '__main__':
    main()