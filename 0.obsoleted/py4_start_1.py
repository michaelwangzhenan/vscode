print("start_1")


def fibonacci(number):
    fibo_list = [1, 1]
    i = 2
    while number - 2 > 0:
        # fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])
        fibo_list[len(fibo_list):] = [fibo_list[i - 1] + fibo_list[i - 2]]
        i += 1
        number -= 1

    for f in fibo_list:
        print(f'{f}, ', end='')

    print()


def fibonacci2(number):
    first = 1
    second = 1
    print(f'{first}, {second}, ', end='')

    while number - 2 > 0:
        third = first + second
        print(f'{third}, ', end='')
        first = second
        second = third
        number -= 1

    print()


def fibonacci3(number):
    first, second = 0, 1
    while number > 0:
        print(f'{second}', end=', ')
        first, second = second, first + second
        number -= 1
    else:
        print()


fibonacci(10)
'''
fibonacci2(10)
fibonacci3(10)

t1 = {}
print(t1, " ", type(t1))
t2 = set()
print(t2, " ", type(t2))
t3 = ()
print(t3, " ", type(t3))
t4 = []
print(t4, " ", type(t4))


def test_para(a):
    print(f'test_para before: a = {a}')
    a = 0
    print(f'test_para after: {a}')


a = 1
print(f'before function: a = {a}')
test_para(a)
print(f'after function: a = {a}')


def test_para2(L):
    print(f'test_para2 before: L =', end=" ")
    for l in L:
        print(l, end=" ")
    print()
    L.append(4)
    print(f'test_para2 after: L = ', end=" ")
    for l in L:
        print(l, end=" ")
    print()


L = [1, 2, 3]

print(f'before function: L = ', end=" ")
for l in L:
    print(l, end=" ")
print()

test_para2(L)

print(f'after function: L = ', end=" ")
for l in L:
    print(l, end=" ")
print()


def fun1(a, b, c=5):
    print(f'a={a},b={b},c={c}')


fun1(1, 2, 3)
fun1(b=2, c=3, a=1)
fun1(1, 2)


def fun2(*var):
    for v in var:
        print(v, end=", ")
    print()


fun2(1, 2, 3)
fun2(1, 2, 3, 4, 5, "a", True)


def fun3(arg1, **var):
    print(arg1, end=" ")
    print(var)


fun3("dict: ", a=1, b=2, c="c")
'''
