# %matplotlib inline
from sklearn.datasets import fetch_lfw_people
import matplotlib.pyplot as plt

people = fetch_lfw_people(min_faces_per_person=20, resize=0.7)

# 先に名前のリストをとっておく
names = []
for t in people.target:
    names.append(people.target_names[t])
print(names[0:10])

# 名前を短くしたいので写真は別の変数に入れる
images = people.images

fix, axis = plt.subplots(2, 3, figsize=(15, 8), subplot_kw={'xticks':[], 'yticks':[]}) # 2行3列に写真を並べたい
axis[0, 0].imshow(images[0]) # サブプロットに写真を表示する
axis[0, 0].set_title(names[0])  # サブプロットのタイトルに名前を表示する
axis[0, 1].imshow(images[1])
axis[0, 1].set_title(names[1])
axis[0, 2].imshow(images[2])
axis[0, 2].set_title(names[2])
axis[1, 0].imshow(images[3])
axis[1, 0].set_title(names[3])
axis[1, 1].imshow(images[4])
axis[1, 1].set_title(names[4])
axis[1, 2].imshow(images[5])
axis[1, 2].set_title(names[5])
plt.show()

"""
上記のコードでは一つずつに対して写真と名前をセットしているが、サブプロットの数が増えてくるとどんどん大変になる。
ループで効率よく処理したいが、axis が 2 次元配列、names/images が 1 次元配列なので、単純なループでは処理できない。

ただし、axis を一次元配列にすれば、names/images/axis が一つのループで書ける
"""

fix, axis = plt.subplots(2, 3, figsize=(15, 8), subplot_kw={'xticks':[], 'yticks':[]}) # 2行3列に写真を並べたい
axis1 = axis.ravel()    # axis を 1 次元配列にする

for name, image, ax in zip(names, images, axis1):   # これで一つのループで書ける
    ax.imshow(image)
    ax.set_title(name)

plt.show()

# スマートである