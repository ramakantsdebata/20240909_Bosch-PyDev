## Set - [Mutable] Unordered Collection of keys (similar, unique, immutable)
## key - hashable

a = 625
print(hash(625))

b = "Test String"
print(hash(b))

b = "TestString"
print(hash(b))

b = "Test String"
print(hash(b))

# c = [1, 2, 3, 4, 5]
c = (1, 2, 3, 4, 5)
print(hash(c))


def IsMutable(obj):
    try:
        hash(obj)
        return False
    except TypeError:
        return True


d = [1, 2, 3, 4, 5]

print(IsMutable(10))
print(IsMutable(a))
print(IsMutable(b))
print(IsMutable(c))
print(IsMutable(d))

st1 = {}
st1 = {1, 2, 3}
st1 = set()
st1 = set(d)

print(st1)

st1.add(6)
print(st1)
st1.update({5, 6, 7, 8})
print(st1)

st1.remove(5)
print(st1)
if 5 in st1:
    st1.remove(5)

st1.discard(5)
st1.add(2)

ret_val = st1.pop()
print(type(ret_val), ret_val)

st1.clear()
print(st1)

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {7, 8, 9}

print(s1.union(s2))
print(s1 | s2)

print(s1.intersection(s2))
print(s1 & s2)

print(s1.difference(s2))
print(s1 - s2)

print(s1.symmetric_difference(s2))
print(s1 ^ s2)



s4 = {3, 4}
print(s4.issubset(s1))
print( s4 <= s1)

print(s1.issuperset(s4))
print(s1 >= s4)

print(s1.isdisjoint(s3))
print(s1&s3 == set())
