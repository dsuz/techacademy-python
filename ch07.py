string_list = ['hoge', 'foo', 'bar']
integer_list = range(1, len(string_list) + 1)
tuple_list = []

for (i, j) in zip(integer_list, string_list):
    t = (i, j)
    tuple_list.append(t)

print(tuple_list)
