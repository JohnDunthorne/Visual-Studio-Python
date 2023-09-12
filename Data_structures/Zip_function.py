list1 = [1, 2, 3]
list2 = [10, 11, 12]

# we are trying to make a list of 3 tuples that include the first item in each list
# so it will look like this
# [(1, 10), (2, 20), (3, 10)]

print(list(zip(list1, list2)))

# you are not limited to lists, you can pass a string in here as well

print(list(zip("abc", list1, "def", list2, "ghi")))
