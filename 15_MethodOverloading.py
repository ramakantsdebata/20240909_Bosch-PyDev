from multipledispatch import dispatch 

@dispatch(int, int)
def add(a, b):
    print("int, int")
    return a + b

@dispatch(str, str)
def add(a, b):
    print("str, str")
    return a + b

@dispatch(int, int, int)
def add(a, b, c):
    print("int, int, int")
    return a + b +c

print(add(1, 2))      # Error without the multipledispatch module in place
print(add("1", "2"))
print(add(1, 2, 3))

'''
int   add(int, int)   --> add_int_int
float add(int, int)   --> add_int_int
int   add(int, int, int)
int   add(int, int, float)
int   add(int, float, int)
'''
