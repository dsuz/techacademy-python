
# %matplotlib inline # jupyter notebook で実行する時はこの行を有効にする
import matplotlib.pyplot as plt

ax = plt.gca()
ax.plot([1, 2], [3, 4], [5, 3], [7, 8], marker='o') 
plt.show()

ax = plt.gca()

plt.show()