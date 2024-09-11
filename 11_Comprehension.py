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

