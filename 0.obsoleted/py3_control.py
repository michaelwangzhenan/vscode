from random import random, randrange

print('py3')


def test_if(x):
    if x > 0:
        print(f'positive:{x}')
    elif x == 0:
        print('zero')
    else:
        print(f'nagtive:{x}')


def test_match_case(x):
    match x:
        case 1:
            print('1')
        case 2:
            print('2')
        case 3 | 4:
            print('3 or 4')
        case _:
            print(f'default:{x}')


endif = False

for i in range(10):
    r = randrange(-10, 10)
    test_if(r)
    if r == 0:
        print("break~~")
        break
else:
    endif = True
    print("End if")

if not endif:
    print('Not End if')

split = 'while' + "-" * 50
print(split)

n = 10
while n > 0:
    test_match_case(randrange(1, 6))
    n -= 1
else:
    print('End while')

n = 10
while n > 0:
    print(n)
    n -= 2
    break

split = 'range' + "-" * 50
print(split)

print('range(10):', end='')
for i in range(10):
    print(i, end='')
print()
print('range(5,10):', end='')
for i in range(5, 10):
    print(i, end='')
print()
print('range(1,10,3):', end='')
for i in range(1, 10, 3):
    print(i, end='')
print()
if None:
    print(None)
else:
    print('not None')

for char in 'PYTHON STRING':
    if char == ' ':
        break
    if char == 'O':
        continue
    print(char, end='')


'''
def is_odd(x):
    if x % 2 == 0:
        return False
    else:
        return True


def change(y):
    if is_odd(y):
        return y + 2007
    else:
        return int(y / 2)


def calc(z, count):
    after_change = change(z)
    print(f'value = {after_change}, count = {count}')
    if after_change != 2008 and count < 500:
        calc(after_change, count+1)
    elif count == 500:
        print('not found in 500 times')
    else:
        print('got it~')


calc(2004, 1)

'''
