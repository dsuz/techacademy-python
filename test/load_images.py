import os
import cv2
import matplotlib.pyplot as plt

file_dir = os.getenv('USERPROFILE') + '\\Pictures\\'    # 画像が置いてある場所を設定している。これは "マイ ピクチャ" を指定している
filename_list = [
    '1.png',
    '480x480.png',
    'p.png',
    'snapshot_03.26.jpg',
    'snapshot_08.18.png',
    'snapshot_05.50.png',
    'snapshot_19.29.jpg',
]   # 画像ファイル名のリスト

image_list = [] # 画像のリスト
for filename in filename_list:
    file_path = file_dir + filename # file_path: ファイルへのフルパス
    if os.path.isfile(file_path):
        image = cv2.imread(file_path)
        image_list.append(image)
    else:
        print('{}: not found.'.format(file_path))   # 指定したファイルが見つからない時はメッセージを表示する

x = 3   # 横に並べる画像の数
y = -(-1 * len(filename_list) //x)  # 縦に並べる画像の数（画像数を x で割って、小数点以下を切り上げている）

# 顔写真を並べた時のやり方と同じ方法で画像を並べる
fix, axis = plt.subplots(y, x, figsize=(7, 7), subplot_kw={'xticks':[], 'yticks':[]})
for image, filename, ax in zip(image_list, filename_list, axis.ravel()):
    ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))   # cv2 で読み込んだ画像をそのまま表示すると日光写真のように見えるので、通常の RGB に変換する
    ax.set_title(filename)

plt.show()
