from pandas import DataFrame


df = DataFrame({'key1': ['a', 'b', 'a', 'b', 'b'],
                'key2': ['1', '3', '2', '1', '3'],
                'data1': [4, 1, 2, 6, 7],
                'data2': [43, 14, 25, 66, 79]})

print("df:")
print(df)

grouped = df['data1'].groupby(df['key1'])
print("grouped:")
# print(grouped)
# print(list(grouped))
# print(grouped.describe())
print(grouped.size())
print(grouped.get_group('a'))
# print(grouped.get_group('b'))
# print(grouped.mean())
