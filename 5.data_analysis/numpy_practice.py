import numpy as np


def ndarray_basic():
    data1 = [1.0, 2.3, 4, 6.6, 0]
    array1 = np.array(data1)
    print(array1, array1.ndim, array1.shape, array1.dtype)

    data2 = [["abc", "abd", "abe"],
             ["123", "124", "125"]]
    array2 = np.array(data2)
    print(array2, array2.ndim, array2.shape, array2.dtype)


ndarray_basic()
