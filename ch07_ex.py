import sys  # 出力のみに使用。提出データには実際は不要

l = ['hoge', 'foo', 'bar']

result = zip(range(1, len(l) + 1), l)

# 以下も出力のみ。課題データには不要
print('[', end='')
for t in result:
    print(t, end='')
print(']')