# import sys
# sys.path.insert(0, "..//..//..//")

from greetings import *

def Test1():
    print(f"Consumer {__name__=}")

    greet()
    greetName("Nikhil")


def Test2():
    from greetings import prepFinal
    print(prepFinal("First", "Second"))


def Test3():
    import greetings
    print(greetings.prepFinal("First", "Second"))

def Test4():
    # from greetings import *   <-- Not allowed in the local scope
    pass


def Test5():
    from mymath.algebra import add
    print(add(1, 2))


# from mymath.algebra import * 
def Test6():
    print(mul(2, 3))

from mymath import *
def Test7():
    print(add(1, 2))

Test6()