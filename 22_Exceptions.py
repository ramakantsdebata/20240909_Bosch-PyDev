class NumberConversionError(ArithmeticError):
    pass



def Bar():
    print("Bar")
    # res = 10/0
    # raise ZeroDivisionError("MESSAGE FOR ZERO DIVISION ERROR")
    raise NumberConversionError("MESSAGE FOR NUMBER CONVERSION ERROR")
    print("returning from Bar")

def Foo():
    print("Foo")
    try:
        Bar()
    except (ZeroDivisionError, OverflowError) as ex: 
        print("A Zero divsion error occurred!")

        print(f"String --> {ex}")
        print(f"String --> ", str(ex))

        print(ex) # print(str(ex))  --> print(ex.__str__())  --> print(ex.__repr__())
        
        print(f"Repr --> {ex!r}")
        print(f"Repr -->", repr(ex))
    except ArithmeticError as ex:
        print("Some Arithmetic exception happened", repr(ex))
    print("returning from Foo")

def Main():
    print("Main")
    Foo()
    print("returning from Main")

Main()