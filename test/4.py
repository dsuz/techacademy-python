abc = ['a', 'b', 'c']
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
aiu = ['あ', 'い', 'う', 'え', 'お']

for x, y, z in zip(abc, num, aiu):
    print (x + ' ' + str(y) + ' ' + z)
