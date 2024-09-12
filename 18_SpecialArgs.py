# / --> Anything to the left of this has to be positional-only
# * --> Anything to the right of this has to be keyworded/named-only

def add(a, b, /, c, d, *, e=0, f):
    return a+b+c+d+e+f

# add(1, 2, 3, 4, 5, 6) # Last 2 args have to be keyworded
add(1, 2, 3, 4, e=5, f=6) 

# add(a=1, b=2, c=3, d=4, e=5, f=6)
add(1, 2, c=3, d=4, e=5, f=6)

add(1, 2, 3, 4, f=6) 


def fn1(*, a, b, c):  # Only named args
    pass


def fn2(a, b, c, /):  # Only positional args
    pass
