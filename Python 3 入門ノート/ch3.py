b = 5

a = 3
a *= b # a * b
print('1. ' + str(a))

a = 99
a /= b # a / b
print('2. ' + str(a))

a = 99
a //= b # a / b の整数値
print('3. ' + str(a))

a = 8
a %= b # a を b で割った余り
print('4. ' + str(a))

a = 3
b = 3
a **= b # a を b 回掛ける
print('5. ' + str(a))
