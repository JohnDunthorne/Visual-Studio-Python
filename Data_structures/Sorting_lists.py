numbers = [3, 15, 25, 4, 5, 2, 34, 100]

# if a list is all jumbled like this you can sort it

numbers.sort()
print(numbers)

# we can sort them in reverse too

numbers.sort(reverse=True)
print(numbers)

# you can also sort a list without modifying it:

numbers = [3, 15, 25, 4, 5, 2, 34, 100]
print(sorted(numbers))  # < they are sorted here
print(numbers)  # < but still intact
print(sorted(numbers, reverse=True))  # < now sorted backwards
print(numbers)  # < but original list preserved

print("-" * 60)
# sorting complex lists:

items = [
    ("product3", 30),
    ("product1", 10),
    ("product2", 20),
    ("product5", 50),
    ("product4", 40),
]
print(items)


# we can make our own function to sort this list
def sort_item(item):
    return item[1]


# now when you call the sort function, and use this function as a reference
# it will try to sort the index of the second item in each tuple (the price)
# so it should sort them by price now

items.sort(key=sort_item)  # key= since sort takes no positional arguements
print(items)
