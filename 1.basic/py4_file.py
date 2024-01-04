from random import randrange

'''
"r"：只读模式，文件不存在则报错，文件指针位于文件开始
"r+": 读+写方式，文件不存在则报错，文件指针位于文件开始

"w"：只写模式，文件不存在则创建。如文件存在，则先清空文件原来内容
"w+":读+写模式，文件不存在则创建。如文件存在，则先清空文件原来内容

'a'：追加模式，不能读。用于在文件末尾添加数据，而不是覆盖原有内容。如果文件不存在，则创建一个新文件。
'a+'：追加模式，可以读。

'x'：独占创建模式。用于创建一个新文件，并在创建时打开该文件进行写入。如果文件已存在，则抛出异常。
'b'：二进制模式。用于以二进制方式读取或写入文件。通常用于非文本文件（如二进制文件、图片等）。
't'：文本模式。用于以文本方式读取或写入文件。默认模式，可省略不写。
'''

'''
seek(offset, whence=os.SEEK_SET)

whence 的可用值有:
os.SEEK_SET 或 0 -- 流的开头, 默认值, offset 应为零或正值
os.SEEK_CUR 或 1 -- 当前流位置; offset 可以为负值
os.SEEK_END 或 2 -- 流的末尾; offset 通常为负值

seek(x, 0) : 表示指针从开头位置移动到x位置
seek(x, 1) : 表示指针从当前位置向后移动x个位置
seek(-x, 2) : 表示指针从文件结尾向前移动x个位置

'''


def open_file_r():
    f = open("file.txt", "r")
    print("open with 'r', postion =", f.tell())
    for line in f:
        # 不能在循环中调用 tell函数，会报 OSError: telling position disabled by next() call
        # print("open with 'r', postion =", f.tell())
        print(line.strip())
    f.close()

    with open("file.txt", "r+") as f:  # 用with open,不需要调用close
        print("open with 'r+', postion =", f.tell())
        f.write("replace\n")
        f.write("replace2")

        f.seek(0)
        content = f.read()

        f.seek(0)
        lines = f.readlines()

    print("")
    print("content:\n" + content + "\n")
    print("lines:")
    for line in lines:
        print(line.strip())
    print("")

    content = 'n/a'
    file = "file.csv"
    try:
        f = open(file, "r")
        content = f.read()
        f.close()
    except FileNotFoundError:
        print(f"{file} is not exist with mode 'r'.")
        try:
            f = open(file, "r+")
            content = f.read()
            f.close()
        except FileNotFoundError:
            print(f"{file} is not exist with mode 'r+'.")
    print(content)


# open_file_r()


def open_file_w():
    f2 = open(r"D:\1_Michael\python\vscode\file.txt", "w")
    print("open with 'w', postion =", f2.tell())
    f2.write("original content is cleared, this is new content")
    try:
        f2.read()
    except OSError:
        print("file can't be read with open mode 'w'")
    f2.close()

    filename = "file_new.txt"
    try:
        f2 = open(filename, "w")
        f2.write("open with w")
        f2.close()
    except FileNotFoundError:
        print(f"{filename} is not exist with mode 'w'.")
    else:  # try代码块成功执行后会 执行 else 代码块
        # 仅在try代码块成功执行时才需要运行的代码，应放在else代码块中
        print("else will be executed when 'try' success")
    finally:  # 无论是否触发异常，都会执行 finally 代码块，可用于清理工作
        print("finally will be executed anyway!")


def open_file_wplus():
    with open("file.txt", "w+", encoding='utf-8') as f2:  # 指定编码格式
        print("open with 'w+', postion =", f2.tell())
        f2.write("original content is cleared again, this is new content")

        try:
            f2.seek(0)  # 要先把文件位置移到开头
            content = f2.read()
        except OSError:
            print("file can't be read with open mode 'w+'")
        print(content)

    with open("file.xls", "w+") as f2:
        f2.write("open file with 'w+")
        f2.seek(0)  # 要先把文件位置移到开头
        print("file.xls : " + f2.readline())


# open_file_w()
open_file_wplus()


def open_file_a():
    with open("file_a.txt", "a+") as f3:
        f3.seek(0)
        if len(f3.readline()) != 0:
            f3.write("\n")
        for i in range(10):
            for n in range(10):
                f3.write(str(randrange(10)))
            f3.write("\n")
        f3.write("--------------------")
        f3.seek(0)
        content = f3.read()
    # f3.read()  # 用with open 的 f3 变量只在 with 代码块内有效，这里已经不能访问
    print(content)

    while 1:
        birthday = input("input your birthday:")
        if birthday == "q":
            break
        if birthday in content:
            print("yes")
            print("there are [" + str(content.count(birthday)) + "] times")
        else:
            print("no")


# open_file_a()


def formart_as():
    with open("AS.txt", "r+") as f_as:
        content = f_as.read()

    with open("AS_formated.txt", "w") as f_formated_as:
        names = content.split(";")
        for name in names:
            f_formated_as.write(name.strip()+'\n')


# formart_as()
