# square brackets [] can be used to make a list that contains multiple objects

letters = ["a", "b", "c"]
numbers = [1, 2, 3]
Booleans = [True, False]

# you can also put lists inside a list

matrix = [[0, 1], [2, 3]]
print(matrix)

# you can crate a list with multiple entries using a multiplier

zeros = [0] * 10
print(zeros)

# you can combine lists by creating a new variable with the two lists in it

combined = zeros + letters + numbers
print(combined)

# to print a range of numbers in a list you can combine list with range:
my_list = list(range(1, 21))
print(my_list)

# we can also list out strings
characters = list("hello world")
print(characters)

# you can use len to return the number of characters in a list
print(len(characters))
print(len(combined))
