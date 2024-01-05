# from cmath import e, pi, sqrt
# from random import choice, uniform

print("py2")
'''
c = choice(range(100))
print(c)
u = uniform(10, 11)
print(u)

print(e)
print(pi)


s = "0123456789"
print(s[0])
print(s[:])
print(s[1:3])
print(s[:3])
print(s[:-3])
print(s[3:])
print(s[-3:])
print(s[::3])
print(s[::])

print(f'constant e={e}, pi={pi}')

List = ["str", 123, False, 1 + 2j]
print(List)
del List[0]
print(List)
List.append("end")
print(List)
print(List.index("end"))
print(len(List))
x = ["End", 'end', 123, "abc"]
for a in x:
    if a in List:
        print(f"{a} in List")
    else:
        print(f"{a} NOT in List")
print(List * 2)

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

list_conbine = [list1, list2]
print(list_conbine[0])
print(list_conbine[1])
print(list_conbine[0][1])
for x in list_conbine:
    for y in x:
        print(y)

list1.extend(list2)
print(list1)
list1.insert(1, '2nd')
print(list1)
list1.pop(1)
print(list1)
list1.remove(1)
print(list1)
list1.reverse()
print(list1)
print(list2)
list2 = list1.copy()
print(f'list2 = {list2}')
list2.remove(2)
list2.remove(3)
print(list2)
list2.sort()
print(list2)
list2.sort(reverse=True)
print(list2)


list_t = [1, 2, 3]
tuple_l = tuple(list_t)
print(type(tuple_l))
list_tuple = list(tuple_l)
print(type(list_tuple))


dictTest = dict()
key = [1, 2, 1, 3, 2]
for k in key:
    if k not in dictTest:
        dictTest[k] = sqrt(k)
    else:
        print(f'{k} is already in the dict: dict[{k}]={dictTest[k]}')
print(dictTest)

d2 = dict.fromkeys(key, "default")
print(d2)
print(d2.get(1))
print(d2.get(5))
print(d2.items())
print(d2.keys())
d2.setdefault(5)
print(d2)
d2.setdefault(1)
print(d2)
d2.setdefault(1, 1)
print(d2)
d2.setdefault(6, 1)
print(d2)
d2.update(dictTest)
print(d2)

print(d2.values())
d2.popitem()
print(d2)
d2.pop(1)
print(d2)


def print_sequence(to_print):
    return f'this is {to_print}'


list_sample = [1, 2, 3, 4]

com = [print_sequence(x) for x in list_sample]
print(com)
print([print_sequence(x) for x in list_sample if x % 2 == 0])

dic_sample = {x: print_sequence(x) for x in list_sample}
print(dic_sample)
print({x: print_sequence(x) for x in list_sample if x > 2})

set_sample = {print_sequence(x) for x in range(10)}
print(set_sample)
print({print_sequence(x) for x in list_sample if x < 2})

tuple_generator = (x for x in range(10))
print(tuple_generator)
print(type(tuple_generator))
tuple_sample = tuple(tuple_generator)

'''
