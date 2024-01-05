print("This is data type practice module: Number, String, Bool, List, Tuple, Set, Dictionary, Bytes")

print('---------->Number<----------')
list2 = b = c = 1
print(list2, b, c)

e, f, g, h, i = "a", True, 1, 1.0, 1 + 2j
print(e, f, g, h, i)
print(type(e), type(f), type(g), type(h), type(i))

del list2, b, c
list2 = -3.14e-3
print(list2)
list2 = 'one hundred'
print(list2)
print(0b1111)  # 二进制
print(0o10)  # 八进制
print(0x10)  # 十六进制

print('4/7 =', 4 / 7)  # 除法，得到一个浮点数
print('4//7 =', 4 // 7)  # 整除
print('4%7 =', 4 % 7)  # 取余
print('2^10 =', 2 ** 10)  # 幂计算

print('---------->String<----------')
testStr = '0123456789'
print(testStr)  # 输出字符串
print(testStr[0:-1])  # 输出第一个到倒数第二个的所有字符
print(testStr[0])  # 输出字符串第一个字符
print(testStr[2:5])  # 输出从第三个开始到第六个的字符（不包含）
print(testStr[2:])  # 输出从第三个开始后的所有字符
print(testStr[1:9:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(testStr * 2)  # 输出字符串两次
print(testStr + 'Hello')  # 连接字符串

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# 字符串前加f，表示格式化字符串(f-string)，允许将变量和表达式嵌入到字符串中，以简化字符串的构建。
# 在格式化字符串中，花括号({})中的任何内容都会被解释为Python表达式，并在字符串中使用它们的值
name = "Michael"
character = 'Cool'
age = 18
print(f"This is {name} who is very {character}, I'm {age} years old.")
print("This is %s who is very %s, I'm %d years old." % (name, character, age))

'''
print('---------->Bool<----------')
t = True
f = False

print(t and f)
print(t or f)
print(not t, not f)
print(int(t))
print(float(t))
print(str(t))
print('......')
print(t == 1)
print(t == 1.0)
print(f == 0)
print(f == 0.0)
print(f == "")
print(f == [])

print('---------->List<----------')
list2 = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list2)  # 输出完整列表
print(list2[0])  # 输出列表第一个元素
print(list2[1:3])  # 从第二个开始输出到第三个元素
print(list2[2:])  # 输出从第三个元素开始的所有元素
print(list2 + tinylist)  # 连接列表
print(list2 * 2)  # 输出两次列表

# 与Python字符串不一样的是，列表中的元素是可以改变的：
list2 = [1, 2, 3, 4, 5, 6]
list2[0] = 9
list2[2:5] = [13, 14, 15]
print(list2)

list2[2:5] = []  # 将对应的元素值设置为 []
print(list2)

s = "this is a sentence."
print(s)
reverse = s.split(" ")  # reverse 是一个list
print(reverse)
reverse = reverse[-1::-1]  # 第一个参数 -1 表示最后一个元素, 第二个参数为空，表示移动到列表末尾,第三个参数为步长，-1 表示逆向
print(reverse)
s = "_".join(reverse)
print(s)

print('---------->Tuple<----------')
# 元组和String一样，元素不能修改
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
connect = tuple + tinytuple  # 连接元组
print(connect)

tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号

print('---------->Set<----------')
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'ABC' in sites:
    print('Runoob is in the set')
else:
    print('Runoob is NOT in the set')

# set可以进行集合运算
a = set('abracadabra')  # set 可以去重
b = set('alacazam')

print('set a =', sorted(a))
print('set b =', sorted(b))
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

print('---------->Dict<----------')
dict_null = {}
print(dict_null)

dict_num = {1: 'one', 2: 'two', 3: 'three'}
print(dict_num)
print(dict_num.keys())
print(dict_num.values())
print(dict_num[2])

dict_str = {}
print(dict_str)
dict_str['one'] = 1
dict_str['two'] = 2
dict_str['three'] = 3
print(dict_str['three'])

# 构造函数 dict() 可以直接从键值对序列中构建字典
dict_bool = dict([(True, 1), (False, 0)])
dict_fruit = dict(a='apple', b='banana', o='orange')
print(dict_bool[True])
print(dict_fruit['o'])

print(dict_fruit)
dict_fruit.pop('a')
print(dict_fruit)
dict_fruit['c'] = 'coconut'
print(dict_fruit)

print('---------->Bytes<----------')
#  Byte = 8 bits ==> 0~255 ==> Bytes 的每个元素都是 0~255
B = b'Hh0'
print(B[0])
print(B[1])
print(B[2])
print(ord('H'))

a = [1, 2, 3]
b = [1, 2, 3]
c = 2e123
d = 2e123
f = 10000
g = 10000
h = 'abcde'
i = 'abcde'
print(id(a) == id(b), id(c) == id(e), id(f) == id(g), id(h) == id(i))

b = a[:]
print('is', id(a) == id(b), a is b)

b = a
d = c
print('is', id(a) == id(b), a is b)
print('a=', a, 'b=', b)
print('c=', c, 'd=', d)

a.append(4)
c = 123
print('a=', a, 'b=', b)
print('c=', c, 'd=', d)


print('is2', id(a) == id(b), a is b)
if a is not b:
    pass
else:
    print('not pass')

del a, b, c
a = 1
print(id(a))
a = 2
print(id(a))

import math
print(math.modf(54.53))
print(round(3.14159265, 2))
'''
