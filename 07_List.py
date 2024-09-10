## List - [Mutable] Ordered Collection of non-homogeneous objects

lst1 = []
lst1 = list()
lst1 = list("String")
print(lst1)


lst1 = list([1, 2, 3, 4, 5])
print(lst1)

lst1 = [1, 2, "Manish" ,"Abhijeet"]
print(lst1[2])

print(id(lst1))
lst1.append("Rakesh")
print(id(lst1))

print(lst1)
print(len(lst1))
print(lst1[-1])
print("Manish" in lst1)

lst2 = [1, 2, 3, 4, 2, 3, 2, 5]
print(lst2.count(2))
print(lst2.index(2))

print(lst1.index("Manish"))

lst3 = lst1 + lst2
print(len(lst3), lst3)
lst3.insert(3, 100)
print(lst3)

lst4 = [10*4]
print(len(lst4), lst4)

lst4 = ["Test"*4]
print(len(lst4), lst4)

lst4 = ["Test", "String"]*4
print(len(lst4), lst4)

print(len(lst4))
print(lst4.__len__())

print(f"{sum(lst2)=}")

it = iter(lst2)  # lst2.__iter__()
# __iter__() returns an iterator 
# Any type (think class) implementing the __iter__() method is an iterable.
# Look up --> generators, iterable, iterator

for val in lst2:
    print(val, end=', ')
print()


print(min(lst2), max(lst2))
# len, min, max, sum, iter, sort, count, index, insert, reverse

print(lst2)
lst2.remove(3)
print(lst2)
lst2.pop(2)
print(lst2)


lst1 = [1, 2, "Manish" ,"Abhijeet"]
del lst1[2]
print(lst1)

###############################################################################################

## str - Immutable
## list - mutable

str1 = "Rakesh"
str2 = str1
print(id(str1), id(str2))

str1 += "!"
print(id(str1), id(str2))
print(str1, str2, sep="\n")


lst1 = [1, 2, 3, 4, 5]
# lst2 = lst1
lst2 = lst1[:]
print(id(lst1), id(lst2), sep="\n")

lst1[1] = 200
print(id(lst1), id(lst2), sep="\n")
print(lst1, lst2, sep='\n')