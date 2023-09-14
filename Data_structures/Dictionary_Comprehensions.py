values = []
for number in range(5):
    values.append(number * 2)
print(values)

# so above here we create an empty list called values
# we then do a for loop, for numbers in a range of 5
# we append the nummber, multiplied by 2
# this returns ***[0, 2, 4, 6, 8]***

# we can use list comprehension to phrase this as
# [expression for item in items]
# the expression is - (number * 2)
# the item is >number<
# and the items is >range(5)<

values = [number * 2 for number in range(5)]
print(values)

# this will return an identical list to that of above
