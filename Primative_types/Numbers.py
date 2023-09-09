# there are 3 types of numbers python deals with, integer, float and complex numbers

# integers are whole numbers
x = 1

# floats are numbers with decimal points
y = 2.3

# complex numbers are something more common with engineers
z = 1 + 2j  # j being an imaginary number (like i in mathematics)

print(f"{x} {y} {z}")

# python contains all the standard aritmatic operations that we use in math

a = 1 + 2  # addition
b = 2 - 1  # subtraction
c = 3 * 3  # multiplication
d = 16 / 2  # division
e = 16 // 2  # double slash will return an integer automatically
f = 10 % 3  # this is modulous (the remainer of a division)
g = 10**3  # this is an exponant in this case 10 to the power of 3
# fmt: off
print(f"this is addition {a} \nthis is subtration {b} \nthis is multiplication {c} \nthis is division {int(d)}")
# fmt: on
# i wrote int(d) so the number gets represented by an integer rather than a float
print(f"this is division with double slash to return an integer not float {e}")
print(f"this is modulous, meaning the remainer after a division {f}")
print(f"this is an exponant {g}")

# augmented assignment operators look like this
# instead of writing
x = x + 3
# to add 3 to the value of x
# we can write
x += 3
# this will do the same thing
