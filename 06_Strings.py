# Strings - [Immutable] collection of characters 

s1 = 'Test'
s2 = "Test"
print(s1, s2)

s1 = "This is Vineet's book."
s2 = 'He said, "Thanks for returning."'

path = r"c:\User\newfile"
print(path)

s3 ='''
This
is a
multiline
comment
'''
s4 = """
This
is a
multiline
comment
"""

usage = """Add Method
add(firstobj: int, secondobj: int) -> int
Considering that the objets passed are integers.
"""

# __doc__ : Help documentation generations  ( more in the topic of functions)

print(usage)

s5 = "First""Second"
print(s5)

# String fully Unicode capable

program = "Python"
duration = 5
fmt = "We are in a %s training for %d days."
s1 = fmt%(program, duration)
print(s1)

print("We are in a %s training for %d days."%(program, duration))

s2 = "We are in a {} training for {} days.".format(program, duration)
print(s2)

s3 = f"We are in a {program} training for {duration} days."
print(s3)

print(f"s3 = {s3}")
print(f"{s3=}")


## Slicing - Chunking up the string 
print(s3[5])
print(s3[len(s3) - 1])
print(s3[-1])           ## Prefer this form
print(s3[5:15])
print(s3[5:])
print(s3[:15])
print(s3[:])
print(s3[:-9])

print(s3[-5:-2])

s4 = "1234567890"
print(s4[2:8:2])
print(s4[7:])
print(s4[-3:])
print(s4[-4:-8:-1])
# 321
print(s4[-8::-1])

# 098
print(s4[:-4:-1])

# 321098
# print(s4[])