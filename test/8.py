# %matplotlib inline # jupyter notebook で実行する時はこの行を有効にする
import matplotlib.pyplot as plt

a = plt.gca()   # a は Axes
a.plot(0.5, 0.5, marker='o') # plot は両方の軸がないとできないので Axes で行う
b = a.get_xaxis()   # b は Axis
b.set_visible(False)    # x 軸の目盛りを非表示にする。x-axis に対して「非表示にする」という操作をしている。
c = a.get_yaxis()   # c は Axis
c.set_label_text('yyyyy')   # y-axis に対して説明のためのラベルを設定している

plt.show()