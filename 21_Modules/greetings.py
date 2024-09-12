__all__ = ["greet", "greetName", "greetInteractive"]

def greet():
    print("Hi there!")

def greetName(name):
    greeting = "Hello"
    finalStr = prepFinal(greeting, name)
    print(finalStr)

def prepFinal(greeting, name):
    return greeting + " " + name + "!!"

def greetInteractive():
    name = input("Enter your name:")
    greetName(name)
    
if __name__ == "__main__":
    greet()
    greetName("Thomas")
    # greetInteractive()

# print(f"Greetings {__name__=}")

