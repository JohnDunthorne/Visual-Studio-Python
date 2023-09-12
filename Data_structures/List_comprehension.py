items = [
    ("product3", 31),
    ("product1", 12),
    ("product2", 23),
    ("product5", 54),
    ("product4", 45),
]

newitems = list(map(lambda item: item[1], items))
print(newitems)

# this was taken from our map function doc
# we can use comprehension to make this even shorter

items2 = [
    ("product3", 31),
    ("product1", 12),
    ("product2", 23),
    ("product5", 54),
    ("product4", 45),
]

newitems2 = [item[1] for item in items2]
print(newitems2)

# as you can see the list comprehension can just run the for loop in one line

price_30_or_above = list(filter(lambda item: item[1] >= 30, items2))
print(price_30_or_above)

# we can filter with list comprehension as well

filtered = [item for item in items2 if item[1] >= 30]
print(filtered)

# this does the exact same as the filter function
