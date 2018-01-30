#リストの情報をタプル化して順番を含めるようにしよう

#リストにいくつかの値が存在するものとします。例えばここでは hoge, foo, bar とします
#これを zip 、 range を必ず使用しましょう
#ここでの順番は1から開始するものとします
#出力結果: [(1, 'hoge'),(2, 'foo'),(3, 'bar')]

#1から連番をつける
x=range(1,4)
y=("hoge","foo","bar")

#zipは複数リストをまとめる。テキストP191
zip_obj=zip(x,y)
xy=tuple(zip_obj)

print('[', end='')
for x in xy:
    print(x, end=',')
print('\b]')
