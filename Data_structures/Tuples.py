# tuples are read only lists, use them if you dont want the list modified at all.

point = (1, 2)  # < tuple are defined by nurmal brackets, not square brakets like lists
point = 1, 2  # < python will treat this as a tuple even without brackets
point = 1  # < python will treat this as an integer
pont = (1,)  # < but with a comma, will treat it like a tuple

# tuple can be concatinated

point = (1, 2) + (3, 4)
print(point)
# ***(1, 2, 3, 4)*** is returned

# you can repeat tuples with multiplication

point = (1, 2, 3) * 3
print(point)
# ***(1, 2, 3, 1, 2, 3, 1, 2, 3)*** is returned

# You can take a list and convert it to a tuple
point = tuple([1, 2])
print(point)
# ***(1, 2)*** is returned

# we can call a specific index like with lists in tuples as well
print(point[1])
# ***2*** is returned
