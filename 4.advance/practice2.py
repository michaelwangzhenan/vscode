from collections import defaultdict
from pprint import pprint
import inspect

# 1 dict.get / dict.setdefault 和 defaultdict


def dict_advance():
    # 在字典中查找某个key时，使用dict[key]， 如果key 不存在会报错。使用dict.get(key)，如果不存在在返回默认值
    dict = {'a': "Alice"}
    print(dict['a'])
    try:
        print(dict['b'])
    except KeyError:
        print("dict['b'] is not exist")

    print(dict.get('b', "Bob"))  # 只是返回一个 default， 不会改变原来的 字典
    try:
        print(dict['b'])
    except KeyError:
        print("dict['b'] is not exist YET")

    dict.setdefault('b', "Bobby")  # 如果 key 不存在则添加一个
    print(dict['b'])

    print('-'*20, "defaultdict", '-'*60)
    # defaultdict 是一个函数，接受一个工厂函数作为参数，生成一个字典。字典的value的类型就是函数返回的类型。
    # 当访问 defaultdict 生成的字典时，如果key 不存在，则返回传入参数类型的default
    # 如： list, set, int, str 都一个工厂函数， default 分别是[], set(), 0, ''
    dict_list = defaultdict(list)
    dict_set = defaultdict(set)
    dict_int = defaultdict(int)
    dict_str = defaultdict(str)

    # 访问不存在的key时，返回传入参数类型的default，并且把这个键值对写入字典
    print(dict_list)
    print(dict_list[0])
    print(dict_list)
    dict_list[0].append('1st')
    dict_list[0].append('2nd')
    print(dict_list)

    print(dict_set[0])
    print(dict_int[0])
    print(dict_str[0])

    def tmp_func():
        return 1

    dict_tmp = defaultdict(tmp_func)  # 也可以用自定义的函数
    print(dict_tmp[0])
    dict_tmp['a'] = "Apple"
    print(dict_tmp[3])
    print(dict_tmp)

    # 字典嵌套
    # nest = lambda: defaultdict(nest)
    # nest_dict = nest()

    print('-'*100)

    def nest2():
        return defaultdict(nest2)

    nest_dict = nest2()
    print(nest_dict)
    nest_dict['a']['Alice'] = 'a.Alice'
    pprint(nest_dict)  # 可以打印出漂亮的 字典
    print(nest_dict['a']['Alice'])

    nest_dict['a']['Bob']['Black'] = 'a.Bob.Black'
    pprint(nest_dict)
    print(nest_dict['a'])
    print(nest_dict['a']['Bob']['Black'])


dict_advance()


# 2 enumerate 函数
def func_enum():
    list_sample = [i for i in range(5)]

    for index, item in enumerate(list_sample):  # 可以自动计数，并取出 index
        print(f"{index}: {item}")

    for index, item in enumerate(list_sample, 100):  # 指定计数起始数字
        print(f"{index}: {item}")


# func_enum()


# 3 对象 ⾃省(introspection)
def introspection():
    list_sample = [1, 2, 3]
    attribue = dir(list_sample)  # 返回⼀个列表，列出了⼀个对象所拥有的属性和⽅法。
    print(attribue)
    print(dir())  # 运⾏dir()⽽不传⼊参数，那么它会返回当前作⽤域的所有名字

    print(type(list_sample))  # type 函数返回⼀个对象的类型
    print(type(attribue))
    print(id(list_sample))  # id 函数返回任意不同种类对象的唯⼀ID
    print(id(attribue))

    # inspect模块也提供了许多有⽤的函数，来获取活跃对象的信息。
    print(inspect.getmembers(list_sample))  # 查看⼀个对象的成员


# introspection()


# 4 推导式(Comprehension)
def comprehension():
    list_squared = [x**2 for x in range(10) if x % 3 == 0]  # 带条件的列表推导式
    print(list_squared)

    list_letter = [chr(97+i) for i in range(26)]  # 不带条件的列表推导式
    print(list_letter)
    dict_letter = {lower: lower.upper() for lower in list_letter}  # 字典推导式
    print(dict_letter)

    set_squared = {x**2 for x in [1, 2, 3, 3, 2, 5, 9]}  # 集合推导式
    print(set_squared)

    tuple_squared = (x**2 for x in [1, 2, 3, 3, 2, 5, 9])  # 元组推导式 返回的是生成器对象
    print(tuple_squared)
    print(tuple(tuple_squared))


# comprehension()


# 5 异常(Exception)
def exception():
    filename = "exception.txt"
    try:
        with open(filename, "r+") as f:
            f.write("excption practice")
            f.seek(0)
            content = f.read()
    except FileNotFoundError as e:
        print(f"open {filename} failed: {e}")
    except (IOError, EOFError) as e:  # 可并列捕获多个异常
        print(f"Io error : {e}")
    except Exception as ex:  # 捕获所有异常, 不知道会抛出什么异常时使用
        print(f"A unkown exception: {ex}")
    else:  # try代码块成功执行后会 执行 else 代码块
        # 仅在try代码块成功执行时才需要运行的代码，应放在else代码块中
        print(f"open {filename} success: {content}")
    finally:  # 无论是否触发异常，都会执行 finally 代码块，可用于清理工作
        print("finally will be executed anyway!")


# exception()


# 6 zip 函数
def func_zip():
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c', 'd']
    tuple1 = ('A', 'B', 'C', 'D', 'E')
    # zip() 函数将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同
    zip_obj = zip(list1, list2, tuple1)
    print(zip_obj)
    print(list(zip_obj))  # 转换成列表

    # zip(*) 为解压, 返回成 tuple
    zip_obj2 = zip(list1, list2, tuple1)
    unziped1, unziped2, unziped3 = zip(*zip_obj2)  # zip_obj 调用过 list(zip_obj) 之后，这里就不能用了，不知道为啥
    print(unziped1)
    print(unziped2)
    print(unziped3)


# func_zip()


# 7 lambda adavance
def lambda_ad():
    list_lambda = [(1, 2), (4, 1), (9, 10), (13, -3)]
    list_lambda.sort()  # 默认是以第一元素为key 排序
    print(list_lambda)

    list_lambda.sort(key=lambda item: item[1])  # 利用lambda 以第二元素为key 排序
    print(list_lambda)

    print("-"*100)

    list1 = [2, 1, 3]
    list2 = ['c', 'b', 'a', 'd']
    zip_list = zip(list1, list2)

    print(list1)
    print(sorted(list1))  # sorted(list1) ==> 返回一个新的排序的列表，原列表不变
    print(list1)

    print(list1.sort())  # list1.sort() ==> 对list1进行排序，但是执行的返回为 None
    print(list1)

    # 利用 lambda 返回两个新的 排序好的列表
    list1, list2 = map(lambda t: sorted(list(t)), zip(*zip_list))
    print(list1, list2)


# lambda_ad()
