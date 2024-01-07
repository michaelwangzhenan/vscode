from collections import Counter


# 1 for ... else
def for_else():
    prime_less100 = []
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                print(f"{i}/{j}={i/j}")
                break
        else:  # 只有 for 循环没有break 时才 进入else
            prime_less100.append(i)
    print(f"prime number : {prime_less100}")


# for_else()


# 2 协程(Coroutine)
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)  # 创建一个协程， 接受 send()⽅法 的传值
        if pattern in line:
            print(line)


def test():
    search = grep('coroutine')
    next(search)  # 启动⼀个协程
    search.send("I love you")
    search.send("Don't you love me?")
    search.send("I love coroutine instead!")
    search.send("bye bye")
    search.close()  # close()⽅法关闭⼀个协程


# test()


# 2 Counter : 就是一个字典，对输入的每个元素进行计数
def counter_():
    file = "3.data_plot/data/death_valley_2018_full.csv"
    with open(file) as f:
        cf = Counter(f)  # 每个文件行作为key，两行一样就计数为2
        print(cf.total())  # 文件的行数


counter_()

# TBD
# C 扩展
# python 2/3 兼容
# 协程(Coroutine)
# 函数缓存(Function caching)
# 上下⽂管理器(Context managers)
