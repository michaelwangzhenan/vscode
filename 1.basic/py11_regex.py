import re


def use_re():
    text = "Apple banana    Orange\t  Pear  \tWatermelon\n"
    print(text.split(" "))  # str 分割文本, 分割后返回列表
    print(re.split('\s+', text))  # 正则表达式分割文本, 分割后返回列表

    regex = re.compile('\s+')  # 先编译好，然后再用
    print(regex.split(text))

    print(re.search('a.', text).group())  # 返回第一个匹配的模式
    print(re.findall('a.', text))  # 返回所有匹配到的模式
    print(re.findall('a(.*?)a', text))  # 匹配2个a 之间的 任意多个任意字符

    print(text.replace('a.', '_X_'))  # str 文本替换
    print(re.sub('a.', '_X_', text))  # 正则表达式文本替换
    print(re.sub('a.', '_X_', text, flags=re.I))  # re.I = re.IGNORECASE


use_re()
