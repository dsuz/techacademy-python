# パターン１
def merge(array2):
    merge_list = []
    array1 = list(range(1, len(array2) + 1))
    for a1, a2 in zip(array1, array2):
        merge_list.append((a1, a2))
    print(merge_list)

# パターン２
def merge2(array):
    merge_list = []
    for i, a in enumerate(array, start=1):
        merge_list.append((i, a))
    print(merge_list)


def main():
    array = ['hoge', 'foo', 'bar']
    merge(array)
    merge2(array)


if __name__ == '__main__':
    main()