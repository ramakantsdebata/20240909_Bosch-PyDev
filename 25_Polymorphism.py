'''class Animal:
    def talk(self):
        print("Tallking...")

class Dog(Animal):
    def talk(self):
        print("woof")

class Cat(Animal):
    def talk(self):
        print("meow")

class Cow(Animal):
    def talk(self):
        print("moo")


def Converse(obj: Animal):
    obj.talk()


def Test1():
    d = Dog()
    c = Cat()
    cw = Cow()

    Converse(d)
    Converse(c)
    Converse(cw)

Test1()
'''

###############################################################################


class Animal:
    def talk(self):
        print("Tallking...")

class Dog:
    def talk(self):
        print("woof")

class Cat:
    def talk(self):
        print("meow")

class Cow:
    def talk(self):
        print("moo")


def Converse(obj: Animal):
    obj.talk()


def Test1():
    d = Dog()
    c = Cat()
    cw = Cow()

    Converse(d)
    Converse(c)
    Converse(cw)

Test1()
