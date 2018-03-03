import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from pandas import DataFrame

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
import seaborn as sns

# file_name = 'coindesk-bpi-USD-close_data-2018-01-10_2018-01-11.csv'
file_name = 'test.csv'
debug = True

# 終値情報を持つcsvから価格を得ます
def importData():
    btc_price = pd.read_csv(file_name)    # DataFrame に CSV を読み込む
    btc_price.head()    # この行は意味がない
    data = np.array(btc_price)  # scikit-learn は pandas (DataFrame) は扱えず、numpy (Array) なら扱えるため、型を変換する。
    return data # ここでは data は２次元配列となっている。

data = np.array(importData())   # ここで再度 numpy.array() をしているが、これには意味はない。data は２次元配列のままである。

# ここでは15時間前までを見るものとします
hour_ago = 15   # 15時間前というのは、データが１時間刻みの場合である。１分刻みの場合は15分になる。

X = np.zeros((len(data), hour_ago)) # データの個数×hour_ago の２次元配列を作り、すべての要素を０で初期化する

# 時間による推移を見て、そこから偏差を学習できるようにします
for i in range(0, hour_ago):
    X[i:len(data), i] = data[0:len(data) - i, 1]

if (debug):
    debug_string = ''
    for i in range(0, len(X)):
        for j in range(0, hour_ago):
            debug_string = debug_string + '{:>5}'.format(str(X[i, j])) + ', '
        debug_string = debug_string + '\n'
    print (debug_string)

Y = np.zeros(len(data)) # 長さ = データの個数 の１次元配列を作り、全ての要素を０で初期化する
# 予測する時間を指定します
predict_time = 1
print (len(X))
print ('X.shape: ' + str(X.shape))
Y[0:len(Y)-predict_time] = X[predict_time:len(X), 0] - X[0:len(X)-predict_time, 0]

if (debug):
    print(Y)

#学習では、50~1800行目を使うものとします。これは情報の偏りを防ぐためのものであり、全体でも構いません
#train_x = X[50:1800,:] # 0 が混ざってしまうので、Xの１次元目は hour_ago より大きくした方がよい
#train_y = Y[50:1800]
train_x = X[20:50,:]

if (debug):
    debug_string = ''
    for i in range(0, len(train_x)):
        for j in range(0, hour_ago):
            debug_string = debug_string + '{:>5}'.format(str(train_x[i, j])) + ', '
        debug_string = debug_string + '\n'
    print (debug_string)

train_y = Y[20:50]
if (debug):
    print(train_y)

# 残りの全てをテストデータとします
#test_x = X[1800:len(X)-predict_time,:] 
#test_y = Y[1800:len(Y)-predict_time]    # Y の最後 predict_time 個の要素は全て 0 なので除外する
test_x = X[50:len(X)-predict_time,:] 
test_y = Y[50:len(Y)-predict_time]


# TODO: LinearRegression を使用して線形回帰モデルで学習させよう。
model = linear_model.LinearRegression()
#train_x = train_x.flatten()
print ('train_x.shape: ' + str(train_x.shape))
model.fit(train_x, train_y)

# TODO: pred_y に対して、テストデータを使用して学習結果を代入しましょう
print ('test_x.shape: ' + str(test_x.shape))
pred_y = model.predict(test_x)

# 予測結果を出力します
result = pd.DataFrame(pred_y) 
result.columns = ['pred_y']
result['test_y'] = test_y

# 結果を output.png に保存します
sns.set_style('whitegrid')
sns.regplot(x='pred_y', y='test_y', data=result)
plt.title('Bitcoin Price')
plt.savefig('output.png')