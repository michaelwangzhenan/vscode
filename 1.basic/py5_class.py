'''
py5 docs
'''


class FirstClass:
    var1 = 0
    var2 = "First"

    def __init__(self):
        pass
        # print(f"__init__():{self}")

    def printClass(self):
        print(f'FirstClass: var1={self.var1}, var2={self.var2}')

    def sum(self, a, b):
        return a + b


def call1stClass():
    first = FirstClass()
    first.printClass()
    first.var3 = False
    print(first.var3)
    first.var1 = 1  # 实例变量
    first.printClass()
    print(FirstClass.var1)  # 类变量
    print(first.var1)

    FirstClass.var1 = 100
    second = FirstClass()
    second.printClass()

    print(FirstClass.var1)

    print("----------")
    first.printClass()


# call1stClass()


class Parent:
    def __init__(self):
        print("Parent__init__")

    def __private(self):
        self.__privateV = "parent.__private"
        print(self.__privateV)

    def _protect(self):
        self._protectV = "parent._protect"
        print(self._protectV)

    def public(self):
        self.publicV = "parent.public"
        print(self.publicV)

    def __repr__(self) -> str:
        return "Parent.__repr__()"


class Son(Parent):
    def __init__(self):
        super().__init__()
        print("Son__init__")

    def public(self):
        self.publicV = "son.public"
        print(self.publicV)
        super().public()


def testHirachy():
    p = Parent()
    # p.__private()
    p._Parent__private()
    print(p._Parent__privateV)
    p._protect()
    print(p._protectV)
    p.public()
    print(p.publicV)

    print("-------------------")
    s = Son()
    s.public()
    s._protect()
    s._Parent__private()
    print(s._Parent__privateV)
    print("-------------------")
    Parent.public(p)
    p.public()
    print("-------------------")
    Parent.public(s)
    print(s.publicV)
    s.public()


# testHirachy()


def testRepr():
    p = Parent()
    print(p)

# testRepr()


# print(__name__)
