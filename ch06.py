import random
# import sys

def generate_random_number_list(list_length):
    """引数で指定された個数の「ランダムな整数」を含んだリストを返す"""
    number_list = []

    for i in range(list_length):
        # number_list.append(random.randint(-sys.maxsize, sys.maxsize))
        number_list.append(random.randint(0, 1000)) # 検算しづらいので範囲を絞った

    return number_list

def average(number_list):
    """引数で指定された整数のリストから、値の平均値を返す"""
    return sum(number_list) / len(number_list)

print('How many numbers do you want to generate?')
buf = input('>>> ')

try:
    number_count = int(buf)
    if number_count > 0:
        number_list = generate_random_number_list(number_count)
        print('generated numbers: ' + str(number_list))
        average_number = average(number_list)
        print('average: ' + str(average_number))
    else:
        print('invalid number.')
except ValueError:
    print('invalid value.')
