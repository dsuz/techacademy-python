# %matplotlib inline # jupyter notebook で実行する時はこの行を有効にする

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, y = make_blobs(random_state=8)

# データの構造を出力しておく
print ('[Data shape]') 
print ('X: ', end='')
print (X.shape) # X は数値のペアのリスト
print ('y: ', end='')
print (y.shape) # y は数値のリスト（分類が入っている。今回は make_blobs() でパラメータ center を指定していないので３種類の分類、つまり 0, 1, 2 のどれかが入っている）

print ('\r\n[Data]\r\nx, y: cluster') # 後で出力する数値データのヘッダー情報を出力する

# y に入っている分類の色に応じて色を変えて、座標をプロットしてみる
for i in range(len(X)):
    plot_color = 'black'

    # make_blobs() でパラメータ center を指定しない場合は分類は３種類なので、それぞれに応じて色を変える
    if (y[i] == 0):
        plot_color = 'red'
    elif (y[i] == 1):
        plot_color = 'green'
    elif (y[i] == 2):
        plot_color = 'blue'
    
    print ('{}, {}: {}'.format(X[i, 0], X[i, 1], y[i])) # 数値データを出力する
    plt.plot(X[i, 0], X[i, 1], color=plot_color, marker='o') # 分類の色でプロットする。パラメータ marker を指定して目立つようにプロットする。

# プロットした内容を表示する
plt.show()
