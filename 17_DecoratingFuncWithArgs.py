def Logger(fnc):
    def Wrapper(*varArgs, **kwArgs):          # Packing any provided args
        Wrapper.__doc__ = fnc.__doc__
        print(f"Calling {fnc.__name__}")
        ret_val = fnc(*varArgs, **kwArgs)     # Unpacking any contents of the collection
        print(f"returned from {fnc.__name__}")
        return ret_val
    return Wrapper

###########################################

@Logger
def greet():
    """Function to greet"""
    print("Hi, how are you?")

@Logger
def add(a, b):
    """Function to add"""
    print("Adding...")
    return a + b

###########################################


greet()
print(add(1, 2)) #, c=3, d=4, e=5))

print(">>", greet.__doc__)
print(">>", add.__doc__)

def SomeFunc(a, b, c):
    """
    This function does something.
    Usage: SomeFunc(in1, in2, in3)
    in1:
    in2:
    in3: 
    """
    print("Does something...")

    # In case of erroneous input, print the usage help and return
    if c == 3:
        print(SomeFunc.__doc__)
        return
    print("Executing normally...")

SomeFunc(1, 2, 3)
SomeFunc(1, 2, 4)
# print(SomeFunc.__doc__)