from pandas import DataFrame


df = DataFrame({'key1': ['a', 'b', 'a', 'b', 'b'],
                'key2': ['1', '3', '2', '1', '3'],
                'data1': [4, 1, 2, 6, 7],
                'data2': [43, 14, 25, 66, 79]})

# print("df:")
# print(df)


def group1():
    grouped = df['data1'].groupby(df['key1'])
    print("grouped:")
    print(grouped)
    # print(list(grouped))
    # print(grouped.describe())
    print(grouped.size())
    print(grouped.get_group('a'))
    # print(grouped.get_group('b'))
    # print(grouped.mean())
    keys = list(grouped.groups.keys())
    print('keys=', keys)
    print('keys[1]= \n', grouped.get_group(keys[1]))

    print('-'*100)
    for key, group in grouped:
        print(key)
        print(group)


def group2():
    grouped2 = df.groupby(df['key1'])
    for key, group in grouped2:
        print(key)
        print(group)
    print(grouped2.groups.keys())
    print(grouped2.get_group('a'))
    print(grouped2['data1'].groups.keys())
    print(grouped2['data1'].get_group('a'))
    print(grouped2['data1'].get_group('b'))


group2()
