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