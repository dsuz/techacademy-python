import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from pandas import DataFrame

import matplotlib as mpl
mpl.use('Agg')

import matplotlib.pyplot as plt
import seaborn as sns

# 終値情報を持つcsvから価格を得ます
def importData():
    btc_price = pd.read_csv('coindesk-bpi-USD-close_data-2018-01-10_2018-01-11.csv')
    btc_price.head()
    data = np.array(btc_price)
    return data

data = np.array(importData())

# ここでは15時間前までを見るものとします
hour_ago = 15

X = np.zeros((len(data), hour_ago))

# 時間による推移を見て、そこから偏差を学習できるようにします
for i in range(0, hour_ago):
    X[i:len(data), i] = data[0:len(data) - i, 1]

Y = np.zeros(len(data))
# 予測する時間を指定します
predict_time = 1

Y[0:len(Y)-predict_time] = X[predict_time:len(X), 0] - X[0:len(X)-predict_time, 0]

#学習では、50~1800行目を使うものとします。これは情報の偏りを防ぐためのものであり、全体でも構いません
train_x = X[50:1800,:]
train_y = Y[50:1800]

# 残りの全てをテストデータとします
test_x = X[1800:len(X)-predict_time,:] 
test_y = Y[1800:len(Y)-predict_time]

#TODO: LinearRegression を使用して線形回帰モデルで学習させよう。
model = linear_model.LinearRegression()
model.fit(train_x, train_y)

#TODO: pred_y に対して、テストデータを使用して学習結果を代入しましょう
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