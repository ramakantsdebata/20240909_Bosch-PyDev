# # a = 1234556
# # b = 1234556

# a = "Test"
# b = "Tes"
# b += "t"

# print(a, b)

# print(a == b)   # Equivalence
# print(a is b)   # Equality
# print(id(a), id(b), sep='\n')

# c = "String"
# print(a == c)
# print(a is c)

# d = 10

# print(type(d) == type(a))

# print(type(a) == type(b))


## Mutability

a = 10
print(id(a), type(a), a)
a += 1
print(id(a), type(a), a)


# Numbers are immutable - Every change will result in recreation of the number object
a = 10
b = 11
c = 10

print(id(a), id(b), id(c))

s1 = "Test"     ; print(id(s1))
s1 += "!!"      ; print(id(s1))
s1 = "String"   ; print(id(s1))

s2 = s1
print(s1 is s2)

s1 += "."

print(s1, s2)