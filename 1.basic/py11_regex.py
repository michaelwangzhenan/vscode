import re


def use_re():
    text = "apple banana    Orange\t  pear  \twatermelon\n"
    splited = re.split('\s+', text)
    print(splited)

    regex = re.compile('\s+')  # 先编译好，然后再用
    splited2 = regex.split(text)
    print(splited2)

    print(regex.findall(text))  # 匹配到的模式


use_re()
