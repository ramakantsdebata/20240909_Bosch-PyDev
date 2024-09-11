## Scope resolution - LEGB
# Local, External, Global, Builtins

def Outer():
    s1 = "Outer String"

    # print(f"{locals()=}")
    # print(f"{globals()=}")
    # print(f"{globals()['s1']=}")

    def Inner():
        # nonlocal s1
        s1 = "Inner String"
        print("Inner -->", s1)

    # Inner()
    print(f"Outer -->", s1)
    return Inner

s1 = "Global String"

# fn = Outer()
# fn()

Outer()()
s2 = "New Global String"

print("Global -->", s1)