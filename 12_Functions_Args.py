'''
def add(a: int, b: int) -> int:
    sum = a + b
    return sum

def sub(a, b):
    pass


res = add(1, 2)
print(res)
print(sub(2, 1))


print(add("1", "2"))
'''

# Define Earlier (Python) vs. Define Higher (Others)


'''
int Bar();      //Declaration

int Foo()
{
    printf("Foo");
    Bar()
}

int Bar()
{
    printf("Bar");
}

int main()
{
    printf("Main");
    Foo();

    return 0;
}
'''

'''
class B;

class A
{
    B* data;
};

class B
{
    A obj;
};


'''

'''
def Bar():
    print("Bar")
    Baz()

def Foo():
    print("Foo")
    Bar()

def Main():
    print("Main")
    Foo()

def Baz():
    print("Baz")

Main()
'''

## Argument Passing ###########################################################
'''
def add(a, b=0, c=0):
    print(f"{a=}, {b=}, {c=}")
    return a + b + c

print(add(1, 2))    # Positional arguments
print(add(3, 4))

print(add(1, 2, 3))
# print(add(1, , 3))        # Error

print(add(b=2, c=3, a=1))       # Named arguments / Keyworded args
print(add(b=2, a=1))
print(add(a=1))
print(add(c=3, a=1))

'''

## Sequence Unpacking and Packing
'''
a, b = 10, 20

seq = [100, 200]
seq = (100, 200)
seq = {100, 200}
a, b = seq          # Unpacking a sequence

# Too many to unpack
# seq = (1, 2, 3)
# a, b = seq

# Not enough values to unpack
# seq = (1, 2)
# a, b, c = seq


seq = (1, 2, 3, 4, 5, 6, 7)
a, b, *c = seq                  # '*' is being used as the 'packing' operator to create a 'list'

print(a, b, c, type(c))
'''

'''
def add(a, b):
    print(f"{a=}, {b=}")
    return a + b


seq = (1, 2)
a, b = seq
print(add(a, b))

print(add(*seq))        # '*' acts as the unpacking operator on the sender side
'''

'''
## Variable arguments {'c' is the var arg}; [Non-Keyworded variable argument list]
def add (a, b, *c):     # '*' is being used as the 'packing' operator to create a 'tuple'
    print(f"{a=}, {b=}")
    print(type(c), c)
    sum = a + b
    for val  in c:
        sum += val
    return sum

print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 4))
'''



## Keyworded Variable argument List ##########################################

def add (a, b, **kwData):
    print(f"{a=}, {b=}")
    print(type(kwData), kwData)
    sum = a + b
    for val  in kwData.values():
        sum += val
    return sum

print(add(1, 2))
print(add(1, 2, c=3))
print(add(1, 2, c=3, d=4))


