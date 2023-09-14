from sys import getsizeof

# Generators use less memory, they are made with () vs [] when creating the list/generator

values = [number * 2 for number in range(1000)]
print("list", getsizeof(values))

# this list of 100 items uses 8856 bytes of data

values = (number * 2 for number in range(1000))
print("list", getsizeof(values))

# this generator uses 208 bytes of data
