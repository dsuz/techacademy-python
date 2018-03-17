# %matplotlib inline

import numpy
import matplotlib.pyplot as plt

data1 = numpy.random.normal(70, 10, 300)    # 適当にランダムなデータを作る

### 普通にグラフを書く
plt.hist(data1)  # ヒストグラムを描く
# グラフのタイトルや軸の説明を設定し、表示する
plt.title('histgram test')
plt.xlabel('x')
plt.ylabel('y')
plt.show()