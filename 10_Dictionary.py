# Dictionary - [Mutable] Unordered collection of key-value pairs
#               key - should be hashable (essentially an immutable)
#               value - can be any type of object
# Set           --> {k1, k2, k3}
# Dictionary    --> {k1:v1, k2:v2, k3:v3}

dt1 = dict()
dt1 = {}
# dt1 = dict({'A'=1, 'B'=2})
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

if (val=dt1.get("std")) is not None:
    print(val)

    
print(dt1)