import numpy as np
from pandas import Series, DataFrame


def series_reindex():
    s1 = Series(np.arange(4), index=['d', 'b', 'a', 'e'])
    print(s1)
    print(s1.reindex(index=['a', 'b', 'c', 'd', 'e']))  # 按指定index 排列，不存在则填NaN
    print(s1.reindex(index=['a', 'b', 'c', 'd', 'e'], fill_value='x'))  # 对不存在的index 填指定值

    s2 = Series(np.arange(0, 8, 2), index=['a', 'c', 'e', 'f'])
    print(s2)
    print(s2.reindex(index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], method='ffill'))  # 不存在填前项值
    print(s2.reindex(index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], method='bfill'))  # 不存在填后项值


# series_reindex()


def dataframe_reindex():
    f1 = DataFrame(np.arange(9).reshape((3, 3)), index=['l1', 'l3', 'l4'],
                   columns=['c1', 'c2', 'c4'])
    print(f1)
    print(f1.reindex(index=['l1', 'l2', 'l3', 'l4'], fill_value=9))  # 重排index
    print(f1.reindex(columns=['c1', 'c2', 'c3', 'c4'], fill_value=9))  # 重排列
    print(f1.reindex(index=['l1', 'l2', 'l3', 'l4'],  # 同时重排
                     columns=['c1', 'c2', 'c3', 'c4'],
                     method='ffill'))


# dataframe_reindex()


def drop_func():
    s = Series(np.arange(4), index=['a', 'b', 'c', 'd'])
    print(s)
    print(s.drop('b'))  # 丢弃一个值
    print(s.drop(['a', 'c']))  # 丢弃多个值

    f = DataFrame(np.arange(9).reshape((3, 3)), index=['l1', 'l2', 'l3'],
                  columns=['c1', 'c2', 'c3'])
    print(f)
    print(f.drop(['l2']))  # 默认drop 行
    print(f.drop(['l1', 'l2', 'l3']))
    print(f.drop('c1', axis=1))  # drop 列需指定 axis=1


# drop_func()


def index_func():
    f = DataFrame(np.arange(9).reshape((3, 3)), index=['l1', 'l2', 'l3'],
                  columns=['c1', 'c2', 'c3'])
    print("f:")
    print(f, '\n')

    print("f['c1']:")
    print(f['c1'], '\n')  # 直接索引返回的是列，一个Series

    print("f[0:1]")
    print(f[0:1], '\n')  # 切片选的是行

    print("f[0:1][['c1', 'c3']]")
    print(f[0:1][['c1', 'c3']], '\n')  # 对行再索引

    print("f.loc['l2']")
    print(f.loc['l2'], '\n')  # loc 选的是行，对应废弃的ix 函数
    print(f.loc[['l2', 'l1']], '\n')  # 选多个行，要传入的是list，也就这这里有两层[[]]

    print("f.loc['l2'][['c1', 'c3']]")
    print(f.loc['l2'][['c1', 'c3']], '\n')  # 同时选取行和列

    print("f > 5")
    print(f > 5, '\n')

    print("f[f > 5]")
    print(f[f > 5], '\n')  # 按元素生成bool值

    print("f['c1'] > 0")
    print(f['c1'] > 0, '\n')

    print("f[f['c1'] > 0]")
    print(f[f['c1'] > 0], '\n')  # bool 切片返回的是行


# index_func()


def auto_align():
    s1 = Series(np.arange(3), index=['a', 'b', 'c'])
    s2 = Series(np.arange(3), index=['a', 'b', 'd'])
    print("s1:")
    print(s1, '\n')
    print("s2:")
    print(s2, '\n')
    print("s1+s2:")
    print(s1+s2, '\n')  # 相同index进行操作，不同的赋值 NaN

    f1 = DataFrame(np.arange(9).reshape((3, 3)), index=['l1', 'l2', 'l3'],
                   columns=['c1', 'c2', 'c3'])
    f2 = DataFrame(np.arange(9).reshape((3, 3)), index=['l2', 'l3', 'l4'],
                   columns=['c1', 'c2', 'c3'])
    print("f1:")
    print(f1, '\n')
    print("f2:")
    print(f2, '\n')
    print("f1+f2:")
    print(f1+f2, '\n')  # 相同二维 index [lx, cy]进行操作，不同的赋值 NaN

    print("f1.add(f2, fill_value=0)")
    print(f1.add(f2, fill_value=0), '\n')  # 使用 DataFrame 的 add 方法时可以指定缺失值， 注意: 指定的时缺失的那个，不是最终的结果

    s3 = f1.loc['l1']
    print("s3 = f1.ioc('l1')")
    print(s3, '\n')
    print("f1-s3")
    print(f1-s3, '\n')  # DataFrame 和 Series 按行运算
    print(f1.sub(s3), '\n')

    s4 = f1['c2']
    print("s4 = f1['c2']")
    print(s4, '\n')
    print(f1.sub(s4, axis=0))  # 按列计算只能用函数并指定轴，如add, sub, mul, div


auto_align()
