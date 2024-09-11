def add(a, b):
    return a + b

def add(a, b, c):
    return a + b +c

# print(add(1, 2))      # Error
print(add(1, 2, 3))

'''
int   add(int, int)   --> add_int_int
float add(int, int)   --> add_int_int
int   add(int, int, int)
int   add(int, int, float)
int   add(int, float, int)
'''
