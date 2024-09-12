# Lambda - Anonymous function
# Functions without name

def square(num):
    return num**2

sq = lambda num : num**2

print(sq(10))

# lambda s1, s2: s1.roll < s2.roll

# sort(coll, lambda s1, s2: s1.roll < s2.roll)

tools = []
tools.append(lambda num : num**0)
tools.append(lambda num : num**1)
tools.append(lambda num : num**2)
tools.append(lambda num : num**3)
tools.append(lambda num : num**4)

print(tools)

# print(tools[0](5))
# print(tools[1](5))
# print(tools[2](5))
# print(tools[3](5))
# print(tools[4](5))

[print(fn(5)) for fn in tools]

IsEven = lambda num: True if num%2 == 0 else False

print(IsEven(5))
print(IsEven(4))
