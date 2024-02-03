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

    print(series4.str.findall('a'))


try_series()


def try_DataFrame():
    data = {'fruit': ['Apple', 'Orange', ' Banana', 'Watermelon'],
            'weight': ['5', '8', '100', '77'],
            'quantity': ['Good', 'Bad', 'Better', 'Perfect']}
    frame = DataFrame(data)
    print(frame)

    frame2 = DataFrame(data, columns=['weight', 'fruit', 'quantity'])  # 指定列的顺序
    print(frame2)

    frame3 = DataFrame(data, columns=['fruit', 'quantity', 'weight', 'taste'],   # 列不存在，值为Nan
                       index=['alpha', 'beta', 'cache', 'delta'])  # 指定 index 名
    print(frame3)
    print(frame3.fruit, type(frame3.fruit))  # 访问列，列是一个Series
    print(frame3['taste'])  # 访问列的另一种方式
    print(frame3.loc['alpha'])  # 选择行， 行也是一个Series
    print(frame3.iloc[0])  # index选择行

    frame3.taste = 'woo!!'  # 设置一列所有值
    frame3['taste']['beta'] = 'ahh~~'  # 设置一个值
    print(frame3)

    frame3.columns.name = 'Summary'  # 列名
    frame3.index.name = 'Index'  # 行名
    print(frame3)
    print(frame3.index)
    print(frame3.columns)
    print(frame3['taste'].index)  # DataFrame 的列共享 Index

    index1 = frame.index
    index3 = frame3.index
    print(index1)
    print(index3)
    indexa = index1.append(index3)  # Index 是不可修改的，函数操作都会返回要一个新的Index
    print(indexa)
    print(index1.difference(index3))
    print(index3.insert(3, 'i'))
    print(index3.isin(indexa))
    print(index3.isin(index1))
    print(indexa.isin(index1))


# try_DataFrame()
