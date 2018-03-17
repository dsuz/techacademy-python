# %matplotlib inline # jupyter notebook で実行する時はこの行を有効にする
import matplotlib.pyplot as plt

ax = plt.gca()
ax.plot(5, 6, marker='o') # (5, 6) に点を打つ
ax.plot([1, 2], [3, 4], marker='o') # (1, 3) - (2, 4) を結ぶ直線を引く
ax.plot([4, 5, 6], [1, 7, 2], marker='o') # 3点を結ぶ線を引く
ax.plot([1, 5, 3, 2], [1, 2, 3, 7], marker='o') # 4点を結ぶ線を引く
y_range = ax.get_ybound()   # 現在のグラフ上の [y の最小値, y の最大値] を取得する
ax.plot([4, 4], y_range) # x = 4 の位置に垂直な線を引く
x_range = ax.get_xbound()   # 現在のグラフ上の [x の最小値, x の最大値] を取得する
ax.plot(x_range, [5, 5]) # y = 5 の位置に水平な線を引く
ax.plot(x_range, [y_range[1], y_range[0]]) # 左上~右下を結ぶ線を引く

# 編集したものを表示する
plt.show()

