# sets are a list of items with no duplicates

numbers = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5]
uniques = set(numbers)
print(numbers)
print(uniques)  # < this will be in curly braces
second = {1, 1, 4, 4, 5}
# ^ we can create a set automatically if we just put all the items in curly braces

print(second)

second.add(6)
print(len(second))
print(second)
second.remove(1)
print(second)

# We can unify 2 set with a | <vertical bar
list = [1, 2, 2, 3, 4, 6, 4, 5, 2, 3, 6, 4, 5, 6, 3, 2, 4, 5, 7]
first_set = set(list)
second_set = {2, 3, 2, 4, 5, 4, 6, 5, 7, 4, 5, 6, 3, 2, 3, 4, 8}

print(first_set | second_set)

# we can see which of the two sets have shared numbers:

print(first_set & second_set)
# ^ this returns {2, 3, 4, 5, 6, 7}, only the numbers that appear in BOTH sets

# you can also see the difference between two sets

print(first_set - second_set)
# this returns the 1, which is in the first set, but not in the second

# we can also see a symetrical difference
print(first_set ^ second_set)

# this shows the 8 and the 1, since the 8 is in second set but not first set
# and the 1 which is in first set, but not second set

# you can check to see if an item is in a list with an if statement
if 8 in first_set:
    print("yes")
else:
    print("no")
