from functools import reduce, wraps
from typing import Any

# 1 *args
# *args 是⽤来发送⼀个⾮键值对的可变数量的参数列表给⼀个函数


def func_variable_parameters(normal, *args):
    print(f"normal={normal}")
    arg_index = 0
    for arg in args:
        print(f"args[{arg_index}]={arg}")
        arg_index += 1


# func_variable_parameters(1, 2, 3, 3, 4, 5)
# func_variable_parameters("a", "b", "c", "d", "e")


# 2 **kwargs
# **kwargs 允许你将不定长度的键值对, 作为参数传递给⼀个函数。 如果你想要在⼀个函数⾥处理带名字的参数, 你应该使⽤**kwargs
def func_key_value_parameters(normal1, normal2, **kwargs):
    print(f"normal1={normal1}, normal2={normal2}")
    print(type(kwargs), len(kwargs))
    for key, value in kwargs.items():
        print(f"key={key}, value={value}")


# func_key_value_parameters("a", 1, v1="v", v2="V", v3=3)
# func_key_value_parameters("b", 2, v3=3, v2="V", v1="v")


# 3 ⽣成器(Generators)
# ⽣成器也是⼀种迭代器，但是只能对其迭代⼀次。这是因为它们并没有把所有的值存在内存中，⽽是在运⾏时⽣成值。
# 要遍历它们，要么⽤⼀个“for”循环，要么将它们传递给任意可以进⾏迭代的函数和结构。
# ⼤多数时候⽣成器是以函数来实现的。然⽽，它们并不返回⼀个值，⽽是yield⼀个值。
def generator(n):
    for i in range(n):
        yield i


def fibo(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


def use_generator(n):
    gen = generator(n)
    for i in gen:
        print(i)


def use_generator2(n):
    gen = generator(n)
    while True:
        try:
            print(next(gen))
        except StopIteration:
            print("no more iter")
            break


def use_generator3(n):
    gen = fibo(n)
    for i in gen:
        print(i)


# use_generator(10)
# use_generator2(10)
# use_generator3(10)


# 4 Map ==> 把列表中的每个元素作为输入传给 指定函数（一般时lambda）进行处理
# Map会将⼀个函数映射到⼀个输⼊列表的所有元素上, map(function_to_apply, list_of_inputs)
def map_list():
    items = [i for i in range(10)]
    squared = list(map(lambda i: i**2, items))
    print(items)
    print(squared)


# map 还可以⽤于函数列表, 列表里的每个函数作为参数传给 lambda
def map_func():
    def add(x):  # 函数中可以定义函数
        return x+x

    def multiply(x):
        return x*x

    funcs = [add, multiply]  # 函数后没有括号，作为变量/对象
    for i in range(10):
        result = list(map(lambda func: func(i), funcs))
        print(result)


# map_func()


# 5 Filter ==> 返回列表中符合指定条件（一般是lambda）的元素
# 过滤列表中的元素，并且返回⼀个由所有符合要求的元素所构成的列表，符合要求即函数映射到该元素时返回值为True
def is_larger(x, y):
    return x > y


def filter_num():
    items = [i for i in range(10) if is_larger(i, 5)]  # 这里的 if 也是某种 filter 吧
    even_num = list(filter(lambda x: x % 2 == 0, items))
    print(even_num)


# filter_num()


# 5 Reduce
'''
reduce() 函数会对参数序列中元素进行累积。
函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function(有两个参数)先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。'''


def add_two(x, y):
    return x+y


def multiply_two(x, y):
    return x*y


def reduce_list():
    items = [i for i in range(1, 5)]
    sum = reduce(add_two, items)
    product = reduce(multiply_two, items)
    print(sum, product)


# reduce_list()


# 6 三元运算
def is_odd(num):
    return True if num % 2 == 1 else False


def test():
    for i in range(10):
        print(f"{i} is odd:", is_odd(i))


# test()


# 7 装饰器(Decorators) ==> 类似 设计模式的的 装饰器(Decorator)模式
# 7.1 函数知识基础
# 把⼀对⼩括号放在后⾯，这个函数就会执⾏
# 如果不放括号在它后⾯，那它可以被到处传递，并且可以赋值给别的变量⽽不去执⾏它
def func_select(flag=True):
    def true_func():
        print("true_func")

    def false_func():
        print("false_func")

    if flag:
        return true_func
    else:
        return false_func


def test_func_select():
    print(func_select())
    print(func_select(False))
    func_select()()
    func_select(False)()
    tf = func_select()
    tf()


# test_func_select()


# 7.2 装饰器函数
def decorator(func):
    @wraps(func)  # @wraps接受一个函数来进行装饰，复制函数名称、注释文档、参数列表等等。让装饰器里面访问装饰之前的函数的属性
    def new_func(*args, **kwargs):
        print("decorator before")
        ret = func(*args, **kwargs)
        print("decorator after")
        return ret  # 返回原函数的返回
    return new_func


@decorator  # 使得调用 origin_func 函数时，变成调用 decorator()
def origin_func(input):
    print(f"origin_func:{input}")
    return f"I'm return for {input}"


def test_decorator():
    origin_func("Hi")
    print("--------")
    print(origin_func("Hi"))


# test_decorator()


# 7.3 带参数的 装饰器 函数
def decorator_args(flag):
    def decorator(func):
        @wraps(func)  # @wraps接受一个函数来进行装饰，复制函数名称、注释文档、参数列表等等。让装饰器里面访问装饰之前的函数的属性
        def new_func(*args, **kwargs):
            print(f"decorator before: {flag}")
            ret = func(*args, **kwargs)
            print(f"decorator after: {flag}")
            return ret  # 返回原函数的返回
        return new_func
    return decorator


@decorator_args(False)  # 使得调用 origin_func 函数时，变成调用 decorator()
def orig_func2(input):
    print(f"origin_func:{input}")
    return f"I'm return for {input}"


# orig_func2("Hi")


# 7.4 装饰器类
# 7.4.1 不带参数的 装饰器类
'''
基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数。
__init__ ：接收被装饰函数；
__call__ ：实现装饰逻辑。
'''


class decorator_func():
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("decorator_func.__call__")
        ret = self.func(*args, **kwds)
        print("do somesting afterwards")
        return ret


@decorator_func
def func(para):
    print(f"func: {para}")
    return f"I'm func's {para}"


# print(func("abc"))


# 7.4.2 带参数的 装饰器类
'''
带参数和不带参数的类装饰器有很大的不同。
__init__ ：不再接收被装饰函数，而是接收传入参数；
__call__ ：接收被装饰函数，实现装饰逻辑。
'''


class decorator_func2():
    def __init__(self, flag) -> None:
        self.flag = flag

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwds):
            print(f"decorator_func2.__call__: {self.flag}")
            ret = func(*args, **kwds)
            self.do_something_afterwards()
            return ret
        return wrapper

    def do_something_afterwards(self):
        print("do_something_afterwards")


class decorator_son(decorator_func2):
    def __init__(self, flag, son_flag) -> None:
        self.son_flag = son_flag
        super().__init__(flag)

    def do_something_afterwards(self):
        super().do_something_afterwards()
        print(f"son : do_something_afterwards -> {self.son_flag}")


@decorator_func2("INFO")
def func2(para):
    print(f"func: {para}")
    return f"I'm func's {para}"


@decorator_son("INFO", "son")
def func2_son(para):
    print(f"func: {para}")
    return f"I'm func's {para}"


# print(func2("abc"))
# print("------------")
# print(func2_son("abc"))
