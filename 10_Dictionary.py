# Dictionary - [Mutable] Unordered collection of key-value pairs
#               key - should be hashable (essentially an immutable)
#               value - can be any type of object
# Set           --> {k1, k2, k3}
# Dictionary    --> {k1:v1, k2:v2, k3:v3}

dt1 = dict()
dt1 = {}
dt1 = dict(A=1, B=2)
print("--> ", dt1)
lst1 = [1, 2, 3, ('a', 'b')]
# lst1 = [1, 2, 3, ('a', 'b', [1, 2, 3])]     # Error: as embedding the list (mutable) means that the key can change
dt1 = dict.fromkeys(lst1)

dt1 = {'A':1, 'B':2}
dt1 = {1: 1, 2: 4, 3: 9, 4: 16}
# dt1 = {A:1, B:2}


print(type(dt1), dt1)


## Retrieve the values
for val in dt1.values():
    print(val, end=', ')
print()

## Retrieve the keys
for val in dt1.keys():
    print(val, end=', ')
print()

## Retrieve the key-value pairs
for key, val in dt1.items():
    print(f"[{key} - {val}]", end=', ')
print()


dt1 = {"roll": 1234, "name": "Ramakant"}
print(dt1["name"])

if "marks" not in dt1:
    dt1["marks"] = 40

if "marks" not in dt1:
    dt1["marks"] = 45

if "marks" in dt1:
    print(dt1["marks"])

if "std" in dt1:
    print(dt1["std"])

try:
    print(dt1["std"])
except KeyError:
    print("No key by that name")


print(f"[{dt1.get("std")=}]")


#if (val:=dt1.get("std")) is not None:
if (val:=dt1.get("std")) != None:
    print(val)
else:
    print("Couldn't find the key.")

# dt1.get("name") = "Vinay"   # get() provides the R-Value, not the L-Value

# dt1["Marks"] = 48


dt1.update({"marks": 50})
print(dt1)

dt2 = {"marks": 55, "std": 7}
print(f"{dt2=}")

dt1.update(dt2)
print(dt1)


print(len(dt1))

# lst = []
# for k in dt1.keys():
#     lst.append(k)
# print("-->", lst)

lst = list(dt1)
print(lst)

print(dt1[lst[0]])

# Nesting a dictionary as a value
addr = {"flat_no": 701, "building": "Kumar", "city": "Coimbatore"}
dt1["addr"] = addr

print(dt1)


# Nesting a dictionary as a key
# Named Tuple - Tuple (immutable) where we can associate names with each element
print("\n", "*"*40)
tp1 = (1, 2, 3)
print(type(tp1), tp1)

from collections import namedtuple

# Point = namedtuple("Point_cls", "x y")
Point = namedtuple("Point", "x y")
p1 = Point(10, 20)
print(f"{p1[0]=}, {p1[1]=}")
print(hash(p1))

print(p1)
print(f"{p1.x=}, {p1.y=}")




# Student = namedtuple("Student_cls", "roll name marks std")
# Student = namedtuple("Student_cls", ["roll", "name", "marks", "std"])
Student = namedtuple("Student", ["roll", "name", "marks", "std"])
s1 = Student(1234, "Vivek", 70, 6)
print(s1)
print(f"{s1.name=}")


dt5 = {p1: 10, s1: 20}
print(dt5)

print(type(p1))
print(type(s1))