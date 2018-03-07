import matplotlib.pyplot as plt

fix, axis = plt.subplots(2, 2) # subplot_kw に何も指定せず既定の目盛りを使う
plt.show()

kw = {'xticks':[], 'yticks':[]} # subplot_kw に何も表示しないよう指定する
fix, axis = plt.subplots(2, 2, subplot_kw=kw)
plt.show()

kw = {'xticks':[0, 0.5, 1.0], 'yticks':[0.2, 0.4, 0.6, 0.8] } # subplot_kw に目盛りを指定する
fix, axis = plt.subplots(2, 2, subplot_kw=kw)
plt.show()
