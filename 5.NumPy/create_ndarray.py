import numpy as np


def print_attribute(ndarr):
    print("ndarray:\n", ndarr)
    print("ndim =", ndarr.ndim)
    print("shape =", ndarr.shape)
    print("size =", ndarr.size)
    print("dtype =", ndarr.dtype)
    print("itemszie =", ndarr.itemsize)


def ndarray_int():
    arr = np.arange(24, dtype=np.int32)
    print_attribute(arr)

    arr_2_12 = arr.reshape(2, 12)
    print_attribute(arr_2_12)

    arr_6_4 = arr.reshape(6, 4)
    print_attribute(arr_6_4)

    arr_2_4_3 = arr.reshape(2, 4, 3)
    print_attribute(arr_2_4_3)

    big_arr = np.arange(10000).reshape(100, 100)
    print_attribute(big_arr)


ndarray_int()


def ndarray_dtype():
    arr = np.array([1.2, 3.5, 5.1])
    print_attribute(arr)

    arr2 = np.array([(1.5, 2, 3), (4, 5, 6)])
    print_attribute(arr2)

    arr3 = np.array([1, 3, 5], dtype=float)
    print_attribute(arr3)

    arr3 = np.array([1, 3+4j, 5], dtype=complex)
    print_attribute(arr3)

    arr5 = np.array([1, 3, 5], dtype=np.int64)
    print_attribute(arr5)


# ndarray_dtype()


def ndarray_init():
    arr = np.array([(1, 2, 3), (4, 5, 6)])

    arr1 = np.zeros((3, 2, 4), dtype=np.int32)
    print_attribute(arr1)
    arr2 = np.zeros_like(arr)
    print_attribute(arr2)

    arr3 = np.ones((3, 2, 4), dtype=np.int32)
    print_attribute(arr3)
    arr4 = np.ones_like(arr)
    print_attribute(arr4)

    arr5 = np.empty((3, 2, 4), dtype=np.int32)  # random value as default
    print_attribute(arr5)
    arr6 = np.empty_like(arr)
    print_attribute(arr6)


# ndarray_init()


def ndarray_linspace():
    arr1 = np.linspace(1, 10, 10)
    print_attribute(arr1)
    arr2 = arr1.reshape(2, 5)
    print_attribute(arr2)

    arr3 = np.linspace(1, 2, 7)
    print_attribute(arr3)


# ndarray_linspace()
