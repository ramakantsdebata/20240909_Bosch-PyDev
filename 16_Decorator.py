def Logger(fnc):
    def Wrapper():
        print("Calling greet")
        fnc()
        print("returned from greet")
    return Wrapper

###########################################

@Logger
def greet():
    print("Hi, how are you?")


# greet = Logger(greet)



###########################################


greet()
# Wrapper()