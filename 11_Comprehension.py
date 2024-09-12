'''
fruits = ["apple", "banana", "cherry", "dragonfruit", "kiwi", "mango"]

fruits_a = []
for fr in fruits:
    if 'a' in fr:
        fruits_a.append(fr)

print(fruits_a)

l = [1]
s = {1}
t = (1,)

print("="*40)
lst = [fr          for fr in fruits       if 'a' in fr]
print(type(lst), lst)

tp = tuple(fr      for fr in fruits       if 'a' in fr)
print(type(tp), tp)

gen = (fr         for fr in fruits       if 'a' in fr)
print(type(gen), gen)

st = {fr          for fr in fruits       if 'a' in fr}
print(type(st), st)

dt = {fr: len(fr) for fr in fruits       if 'a' in fr}
print(type(dt), dt)

print("="*40)



print("\n\n")
print("*"*40)

squares = []
for i in range(1, 11):
    squares.append(i**2)

print(squares)

square = tuple(i**2 for i in range(1, 11))

print(square)

'''

from typing import Any


lst = []
# print(dir(lst))
print(dir(list))

print(dir(int))

print("-"*40, "\n")

public_members = [member for member in dir(int) if member.startswith("_") is False]
print(len(public_members), public_members)

public_methods = [member for member in dir(int) if member.startswith("_") is False 
                  and callable(getattr(int, member))]

callable(getattr(int,'as_integer_ratio'))

print(len(public_methods), public_methods)

'''
def add(a, b):
    return a + b


print(type(add))
add()
'''

'''__call__

class Test:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print()

t1 = Test()

t1(10, 20)
'''


fruits = ["apple", "banana", "cherry", "dragonfruit", "kiwi", "mango"]
# [fr                                                         for fr in fruits       if 'a' in fr]
[print("Present")  if 'a' in fr else print("Absent")        for fr in fruits]
