## Tuple - [Immutable] Ordered collection of non-homogeneous object
#           Can perform all the operations that can be on a list, except for the modifying ones
#           like append, insert, pop, remove, del

tp1 = tuple()
tp1 = ()
print(type(tp1))

# List of one element
lst = [1]
print(len(lst), type(lst))

tp = (1,)       # tuple with only one element declared will require a comma in it
                # to distinguish it from an simple expression resolution.
print(type(tp))
# print(len(tp), type(tp))

tp = (1, 2, 3, 4, 5)
print(tp)

lst = [1, 2, 3, 4, 5]
tp = tuple(lst)
print(tp)