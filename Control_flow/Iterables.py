print(type(5))  # this is show 'int' when ran
print(type(range(5)))  # this will show 'range' when ran

# ranges are complex types that are iterable
for x in range(10):
    print(x)
# range changes the value of x over 10 interations starting from 0 in this case (can be changed)
# by changed the start and end ranges (1, 11) for instance
for y in range(2, 20):
    print(y)
# add a third number to affect how much the interations jump, put a 2 here to only show evey other number
# from the starting range
for z in range(2, 42, 2):
    print(z)
# this will return 2 to 40, but only every 2 numbers
