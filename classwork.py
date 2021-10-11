# my_list = [1, 2, 3, 2, 4, 3, 5, 5, 5, 4, 5]

# s = set(my_list)
# print(s)

# # new_list = list(set(my_list))
# new_list = set((1,3,299))
# print(new_list)

# union_set = set.union(new_list, s)
# union_set.add(77)
# print(union_set)
# print(len(union_set))

# union_set.update([44,33,11,22])
# union_set.discard(100)
# union_set.remove(22)
# print(union_set)

# f_s = frozenset(union_set)
# print(f_s)

# # for item in f_s:
# #     print(item)

# n_set = set(f_s)
# print(n_set == f_s)
# n_set.add(9999)
# print(1 in n_set)
# print(n_set == f_s)

# ---------- string ----------
# s = ' semo teXt     '.strip(' ')
# # .capitalize().lower().upper().title().center(20, '*')
# s = s.replace('e', 'd', 5)
# print(s)
# print(s.find('r'))
# print(s.rfind('t'))
# print(s.index('d'))
# l = list(s)
# print(l)
# l[0] = 'R'
# print(''.join(l))

# ----------- functions -------------
# def func(x: int, y = 0) -> int:
#     """
#     Description of my function
#     """
#     return x + 5 + y

# print(func(y=2, x=5))

# def myFunc(x, y, *args, **kwargs):
#     print(x, y, args, kwargs)
#     print(args[0])
#     print(enumerate(args))
#     for index, item in enumerate(args):
#         print(index, item)

# myFunc(1, 2, 3, 4, 5, key = 'value')

# a = lambda x, y = 10: x + y
# print(a(5, 5))

# x = 0
# def gen():
#     try:
#         yield 1
#         yield 2
#     except StopIteration as e:
#         print(e, 'Data is empty!')


# a = gen()

# print(next(a))
# print(next(a))


# a = iter([1, 2, 3])

# def foo(limit=10):
#    i = 0
#    while True:
#        yield i
#        i += 1
#        if i > limit:
#            raise StopIteration()
# a = foo(2)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# def fun():
#     return [1, 2, 3]

# import lib.modul as modul
# from lib import modul

# x = modul.suma(1,2,3,5)

# from lib.modul import suma
from lib.modul import *
x = suma(1,2,3,5)
print(x)
print(CONST_VALUE)
