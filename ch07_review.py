list1 = ['hoge', 'foo', 'bar'] #元ネタ
list0 = [] #空のリスト

for i in range(1, 4):
    for z in zip(str(i), list1):
        list0.append(z)

print(list0)
