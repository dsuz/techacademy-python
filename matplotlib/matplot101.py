import numpy
import matplotlib.pyplot as plt

data1 = numpy.random.normal(70, 10, 300)    # 適当にランダムなデータを作る
data2 = numpy.random.normal(20, 20, 300)
data3 = numpy.random.normal(50, 30, 300)
data4 = numpy.random.normal(98, 85, 300) 

### 普通にグラフを書いてみる。２つのグラフを重ねてみる
plt.hist(data1, color='red', alpha=.5)  # ヒストグラムを描く
plt.hist(data2, color='blue', alpha=.5) # 別のデータで重ねてヒストグラムを描く。重ねるために色を変えて alpha で半透明にしている
# グラフのタイトルや軸の説明を設定し、表示する
plt.title('histgram test')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

### 複数のグラフをレイアウトして並べてみる
fig = plt.figure()
ax1 = fig.add_subplot(3, 3, 1)  # サブプロット（グラフ）を作り、レイアウトする - 3x3 分割の 1 番（左上）にグラフを置く
ax1.hist(data1) # データを与えてヒストグラムを描く
ax2 = fig.add_subplot(3, 3, 6)  # 2つ目のグラフを作る - 3x3 分割の左上から数えて６番目の場所にグラフを置く
ax2.hist(data2)
ax3 = fig.add_subplot(3, 3, 8)  # 3x3 分割の左上から数えて8番目の場所にグラフを置く
ax3.hist(data3)
plt.show()  # 表示する

### 縦横２つずつ、計４つのグラフを並べてみる
fig2, axes = plt.subplots(2, 2)
axes[0, 0].hist(data1) # 左上にレイアウトされたグラフ
axes[0, 0].set_title('data1')
axes[0, 1].hist(data2) # 右上（以下同文）
axes[0, 1].set_title('data2')
axes[1, 0].hist(data3) # 左下（以下同文）
axes[1, 0].set_title('data3')
axes[1, 1].hist(data4) # 右下（以下同文）
axes[1, 1].set_title('data4')
plt.show()

### 直前の例をループを使ってかっこつけたやり方でやってみる
data_list = [data1, data2, data3, data4]    # ループを使うのでデータはリストに入っている必要がある
fig3, axes2 = plt.subplots(2, 2)
ax = axes2.ravel()  # 縦横２つずつのグラフが２次元配列に入っているが、ループで処理したいので１次元配列として（直列に）並べる

# ループでデータやタイトルをセットしていく
for i in range(4):
    ax[i].hist(data_list[i])
    ax[i].set_title('data' + str(i + 1))
    ax[i].set_xlabel('x axis')
    ax[i].set_ylabel('y axis')

plt.show()
