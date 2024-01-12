import numpy as np


def operation():
    a = np.array([10, 20, 30, 40])
    b = np.arange(1, 5)

    print(a+b)  # 数组上的算术运算符会应用到元素级别
    print(a-b)
    print(a*b)
    print(a/b)
    print(a**2)
    a += 10  # +=, *=会更直接更改被操作的矩阵数组而不会创建新矩阵数组。
    print(a)
    b *= 100
    print(b)
    b += a
    print(a, b)


# operation()


def matrix_operation():
    # 矩阵乘积可以使用@运算符 或 dot函数方法执行
    A = np.array([[1, 1], [0, 1]])
    B = np.array([[2, 0], [3, 4]])

    print(A@B)
    print(A.dot(B))


# matrix_operation()


def random_test():
    b = np.random.random((2, 3))  # Return random floating point number in the range 0.0 <= X < 1.0
    print(b)


# random_test()


def ndarray_function():
    # 许多一元操作，例如计算数组中所有元素的总和，都是作为ndarray类的方法实现的。
    a = np.arange(1, 10)
    print(a.sum(), a.max(), a.min())

    b = np.random.random((2, 3))  # Return random floating point number in the range 0.0 <= X < 1.0
    print(b)
    print(b.sum(), b.max(), b.min())


# ndarray_function()


def ndarray_axis():
    print("a--"*20)
    a = np.arange(12).reshape(3, 4)  # axis 0/1 分别 对应 3/4
    print(a)
    print(a.max(axis=0))  # max of each column
    print(a.max(axis=1))  # max of each row
    print(a[1, 1])  # 第二行，第二列的元素
    print(a[:, 1])  # 所有行，第二列
    print(a[:2])  # 前两行，所有列， 等价print(a[:2, :])
    print(a[:2, :])

    # print("b--"*20)
    # b = np.arange(24).reshape(2, 3, 4)  # axis 0/1/2 分别 对应 2/3/4
    # print(b)
    # print(b.max(axis=0))
    # print(b.max(axis=1))
    # print(b.max(axis=2))


# ndarray_axis()


def pi_calc():
    a = np.arange(1, 20)
    print(3.14*a)
    print(3.14*a**2)


pi_calc()
