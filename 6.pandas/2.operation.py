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

    print("f.loc['l2'][['c1', 'c3']]")
    print(f.loc['l2'][['c1', 'c3']], '\n')


index_func()