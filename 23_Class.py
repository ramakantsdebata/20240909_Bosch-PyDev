from random import randint

# class Test:
#     pass


class Car:
    count = 0       ## Class Variable

    ## Create an object from a type
    # def __new__(cls) -> Self:
    #     pass

    ## Initialise an object already created, immediately after creation
    def __init__(self, make, model, year, color) -> None:
        self.IsRunning = False
        self.make = make
        self.model = model
        self.year = year
        self.__color = color
        self.serial = Car.genSerial()

        # count = count + 1
        Car.count += 1


    def start(self):
        print(f"starting the {self.make}-{self.model}")
        self.IsRunning = True

    def stop(self):
        print(f"stopping the {self.make}-{self.model}")
        self.IsRunning = False

    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}, {self.__color}, {self.serial}"

    def __repr__(self):
        return f"{self.__class__.__name__}, {id(self)}, {self.IsRunning}"

    # def getCount(self):
    #     # return self.count
    #     return self.__class__.count


    @classmethod
    def getCount(cls):
        return f"{cls.__name__}-{cls.count}"

    @staticmethod
    def genSerial():
        return randint(10000, 99999)

    def getColor(self):
        return self.__color
    
    @property
    def Color(self):
        return self.__color
    
    @Color.setter
    def Color(self, value):
        self.__color = value

###############################################################################

class GearedCar(Car):
    def __init__(self, gears, make, model, year, color) -> None:
        super().__init__(make, model, year, color)
        self.gears = gears

    @property
    def Gears(self):
        return self.gears
    
    def __str__(self):
        return super().__str__() + f", {self.gears}"

###############################################################################

def Test1():
    print(f"{Car.count=}")
    c1 = Car("Honda", "Accord", 2024, "Black")
    c1.start()

    c2 = Car("Toyota", "Camry", 2021, "White")
    c2.start()

    c1.stop()
    c2.stop()


    print(c1)   # str(c1) --> c1.__str__()  --> c1.__repr__() --> If not implemented, provides default implementation of object information
    print(repr(c1))


    print(c1, c2, sep="\n")
    print(f"{Car.count=}")
    # print(f"{c1.getCount()=}")
    print(f"{Car.getCount()=}")

    '''
    print(c1.getColor())
    c1.setColor("Yellow")
    print(c1.getColor())

    # print(c1.__color)
    c1._Car__color = "Blue"
    print(c1._Car__color)
    print(c1.getColor())

    print(c1.__dict__)
    '''

    print(c1.Color)
    c1.Color = "Blue"
    print(c1.Color)

def Test2():
    gc1 = GearedCar(7, "Honda", "Accord", 2024, "Black")
    print(gc1)

    print(gc1.getCount())
    print(GearedCar.getCount())
    print(Car.getCount())


Test2()