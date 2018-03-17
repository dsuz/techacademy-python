import numpy as np

a = np.array([1, 2, 3, 4, 5])
print ('a has {} dimensions'.format(a.ndim))
for i in range(len(a)):
    print(a[i], end = ', ') # 一次元だから添字はひとつ
print()

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # 二次元だから角括弧は２重 [[]]
print ('b has {} dimensions'.format(b.ndim))
for i in range(len(b)):
    for j in range(len(b[i])):
        print (b[i, j], end=', ')   # ２次元だから添字は２つ
print()

c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # ３次元だから角括弧が三重 [[[]]] になっている
print ('c has {} dimensions'.format(c.ndim))
for i in range(len(c)):
    for j in range(len(c[i])):
        for k in range(len(c[i, j])):
            print (c[i, j, k], end=', ')    # ３次元だから添字はみっつ
print()