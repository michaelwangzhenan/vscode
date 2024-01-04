from random import randrange


def stringHandle():
    print(r"this is a line with \n")  # 使用 r 可以让反斜杠不发生转义
    number = 5
    print(f"the number is {number}")  # python3.6, 使用 f 可以使用变量格式化字符串
    print("the number is %d" % (number))
    print("the number is {}".format(number))  # python 3.5 and before
    text = "the number is {n1} and {n2}"
    print(text)
    print(text.format(n1="5", n2="6"))

    for i in range(5):
        print(i, end=" ")  # end可以用于将结果输出到同一行
    print("\n")

    Hello = "Hello, you"
    print(Hello.title())  # 回原字符串的标题版本，其中每个单词第一个字母为大写，其余字母为小写
    print(Hello.upper())
    print(Hello.lower())
    print(Hello.count("l"))
    print(Hello.title(), Hello, Hello.title() == Hello)

    str_strip = " hi strip "
    print("'" + str_strip.strip() + "'")
    print("'" + str_strip.lstrip() + "'")
    print("'" + str_strip.rstrip() + "'")

    string1 = "I'm a string"
    string2 = 'This is a "book"'
    print(string1 + "\n" + string2)

    name = "Michael"
    words = "I'm so cool!"
    words2 = "I feel good."
    print(f"Hi, {name}")
    print(name, name.lower(), name.upper(), name.title())
    print(f"{name} said : {words}")
    print(f"{name} said :\n\t{words}\n\t{words2}")

    print(123_000 == 123000, 123_000)  # 下划线没有意义，辅助阅读


# stringHandle()


def dataType():
    T_number = 1
    T_bool = True
    T_str = "abc"  # 不可改变
    T_list = [1, True, "abc"]  # 元素可改变
    T_tuple = (1, True, "abc")  # 元素不可改变
    T_set = {1, True, "abc"}  # 元素可改变
    T_dictionary1 = {0: "1", True: "True", "abc": "abc"}  # 元素可改变

    tup1 = ()    # 空元组
    tup2 = (20,)  # 一个元素，需要在元素后添加逗号
    set1 = set()  # 创建一个空集合必须用 set()
    dict1 = {}  # 创建一个空字典。

    print(T_number, T_bool, T_set, T_dictionary1, tup1, tup2, set1, dict1)
    print(T_dictionary1.get(100, "not exist"))
    # print(T_dictionary1[100]) # 在字典中查找某个key时，使用dict[key]， 如果key 不存在会报错。使用dict.get(key)，如果不存在在返回默认值
    print(T_dictionary1["abc"])
    print(T_dictionary1.get(False, "not exist"))
    print(T_dictionary1.get("abc", "not exist"))

    for key in T_dictionary1.keys():
        print(key, ":", T_dictionary1[key])

    for key, value in T_dictionary1.items():
        print(key, ":", value)

    if "1" in T_str:
        print("true")
    else:
        print(False)
    if 1 in T_list:
        print("true")
    if 1 in T_tuple:
        print("true")
    if 1 in T_set:
        print("true")

    for x in T_str:
        print(x)

    orig_list = ['a', 'd', 'b']
    sorted_list = sorted(orig_list)
    print(orig_list)
    print(sorted_list)
    orig_list.append('x')
    orig_list.insert(3, 'y')
    print(orig_list)
    del orig_list[0]  # 删除一个元素
    print(orig_list.pop(1))  # 弹出一个元素
    orig_list.remove('x')  # 按元素值删除
    print(orig_list)
    if x in orig_list:
        orig_list.remove('x')  # 删除不存在的会出错
    orig_list.insert(0, 'w')
    orig_list.append('a')
    print(orig_list)
    orig_list.sort()  # 永久修改列表
    print(orig_list)
    orig_list.sort(reverse=True)
    print(orig_list)
    print(sorted(orig_list))  # 不修改原列表，返回sort 后的列表
    print(sorted(orig_list, reverse=True))
    o2 = orig_list  # 这是起了一个别名，也就是引用二不是复制
    print(o2)
    print(len(o2))
    o2.append('j')
    orig_list.append('i')
    print("ori=", orig_list)
    print("o2=", o2)

    o3 = orig_list[:]  # 这才是拷贝
    o3.append('m')
    print("ori=", orig_list)
    print("o3=", o3)
    print("o3 1st 3=", o3[:3])
    print("o3 mid 3=", o3[len(o3) % 3:len(o3) % 2+3])
    print("o3 last 3=", o3[-3:])
    r = range(1, 10)
    li = list(r)
    print(r, type(r), li, type(li))
    print(min(r), min(li), max(r), sum(li))
    l2 = [value**3 for value in range(1, 100, 3)]
    print(l2, type(l2))
    s2 = {value for value in range(1, 100, 3)}
    print(s2, type(s2))
    g2 = (value for value in range(1, 100, 3))   # 返回的是生成器对象
    print(g2, type(g2))
    t2 = tuple(g2)
    print(t2, type(t2))


# dataType()


def iterate():
    list = [x for x in range(2)]
    it = iter(list)
    print(it)
    print(next(it))
    print(next(it))
    try:
        print(next(it))
    except StopIteration:
        print("iter is end.")


# iterate()


def test_ut(server, remote):
    return server + ":" + remote


def input_test():
    target = randrange(100)
    while 1:
        guess = input("guess a number 0~99: ")
        if not guess.isdigit():
            print("please input a number")
            continue
        if int(guess) == target:
            print(f"Great! you got it, it's {target}")
            conti = input("try again?")
            if conti == 'yes':
                target = randrange(100)
                continue
            else:
                print("thank you, bye~")
                break
        elif int(guess) < target:
            print("too small")
        else:
            print("too large")


# input_test()
