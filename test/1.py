from sklearn import datasets
from sklearn import svm
import numpy as np

boston = datasets.load_boston()
x = boston.data
y = np.asarray(boston.target, dtype=np.int32)   # 配列の要素（少数）を整数に切り捨てて配列に入れる
n_train = len(x)//2
x_train, x_test = x[:n_train], x[n_train:]
y_train, y_test = y[:n_train], y[n_train:]
clf = svm.SVC()
print(y_train[:10]) # 配列の先頭 10 個を出力する
clf.fit(x_train, y_train)
print (clf.score(x_test, y_test));
