'''
def Outer():

    def Inner():
        pass

    return Inner

fn = Outer()
fn()
'''

# num ** exp

def power_of(exp):
    greet = "Hi"
    def raised_to(num):
        day = "Today"
        print(greet, day, end='')
        return num ** exp
    
    return raised_to


square = power_of(2)        # pass 'exp'
print(square(10))           # pass 'num'

cube = power_of(3)
print(cube(10))

print(power_of(4)(10))

print(square(10))
print(cube(10))

print(type(square))