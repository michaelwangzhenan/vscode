from pandas import Series, DataFrame


def try_series():
    input1_list = ["Alice", "Bob", "Claire", "David", "Ema"]
    print(input1_list.index('Alice'))
    enum = enumerate(input1_list)  # enumerate 也可以为序列创建索引
    for i, v in enum:
        print(i, v)

    print("series", "-"*40)
    series1 = Series(input1_list)  # Series 对象创建一个默认索引
    print("series1:\n", series1)
    print("index:\n", series1.index)
    print("values:\n", series1.values)

    input2_list = range(1, 6)
    series2 = Series(input2_list, index=['a', 'b', 'c', 'd', 'e'])  # 指定index
    print(series2)
    print(series2.index)
    print(series2['c'])
    print(series2[['a', 'e']])
    print(series2 > 3)  # 数组运算应用与 value 上， index 不变
    print(series2 * 5)

    input3_dic = {'A': "Apple", 'B': "Banana", 'O': "Orange"}
    series3 = Series(input3_dic)  # 字典转换为 Series
    print(series3)
    dic_index = ['B', 'C', 'O']
    series4 = Series(input3_dic, index=dic_index)  # 指定索引从字典中取的数据，不存在就是NaN
    print(series4.isnull())  # 数据是否缺失

    print(series3+series4)  # 自动对齐相同的 index

    series4.name = "series4"
    series4.index.name = "series4_index"
    print(series4)

    series4.index = [1, 2, 3]  # 通过赋值修改 index
    print(series4)


# try_series()



def try_DataFrame():



try_DataFrame()