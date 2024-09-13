# MRO - Method Resolution ORder
class A:
    def __init__(self) -> None:
        print(f"Initialising the class '{self.__class__.__name__}")

    def __str__(self):
        return f"Class '{self.__class__.__name__}'"

class B(A):
    def __init__(self) -> None:
        # Do something
        print("B - Super --> ", super())
        super().__init__()
        print(f"Initialising the class '{self.__class__.__name__}")

    def __str__(self):
        return f"Class '{self.__class__.__name__}'"

class C(A):
    def __init__(self) -> None:
        # Do something
        print("C - Super --> ", super())
        super().__init__()
        print(f"Initialising the class '{self.__class__.__name__}")

    def __str__(self):
        return f"Class '{self.__class__.__name__}'"

class D(C, B):
    def __init__(self) -> None:
        # Do something
        print("D - Super --> ", super())
        super().__init__()
        print(f"Initialising the class '{self.__class__.__name__}")

    def __str__(self):
        return f"Class '{self.__class__.__name__}'"

###############################################################################

def Test1():
    d = D()

    print(d)
    print(d.__class__.__bases__)
    print(d.__class__.__mro__)

Test1()
