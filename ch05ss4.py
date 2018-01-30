a = 5
b = 0

try:
    c = a / b
    print (c)
except ZeroDivisionError:
    print('ゼロでは割れないよ')
