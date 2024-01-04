import os
import sys
import getpass

currentDir = os.path.abspath('.')
print(currentDir)
print(len(os.listdir(currentDir)))

currentFile = os.path.abspath(__file__)
print(currentFile)

print(os.path.isdir(currentDir))
print(os.path.isdir(currentFile))
print(os.path.isfile(currentDir))
print(os.path.isfile(currentFile))
print(os.path.exists(currentDir))
print(os.path.exists(currentFile))
print(os.path.exists(os.path.join(currentDir, "prac.py")))
print(os.path.dirname(currentDir))
print(os.path.dirname(currentFile))
print(os.path.join(currentDir, "main.py") == currentFile)
print(os.path.splitext(currentFile))
print(os.path.sep)

print(__name__)

str = "prefix-root-list/{toolchain}/toolchain"
print(str)
print(str.format(toolchain="sm4"))


# print(dir())
# print(__name__)
# print(dir(os))
# print(help(os))


def os_path():
    print(sys.argv[0])
    print(os.path.abspath(sys.argv[0]))
    print(os.path.dirname(os.path.abspath(sys.argv[0])))
    print(getpass.getuser())


# os_path()
