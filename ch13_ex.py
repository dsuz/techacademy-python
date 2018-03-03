f = open('./ch13.txt')

data = f.read().split(" ")
f.close()

dic = {}

for word in data:
    if word in dic.keys():
        dic[word] += 1
    else:
        dic[word] = 1
print(dic)