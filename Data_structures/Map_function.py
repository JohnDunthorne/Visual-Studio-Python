items = [
    ("product3", 30),
    ("product1", 10),
    ("product2", 20),
    ("product5", 50),
    ("product4", 40),
]

# we are taking this list and reducing it to a list of prices only

prices = []
for item in items:
    prices.append(
        item[1]
    )  # < this will append the second object in each tuple (the price)

print(prices)

items2 = [
    ("product3", 31),
    ("product1", 12),
    ("product2", 23),
    ("product5", 54),
    ("product4", 45),
]

# alternatively we can use the map function to do this

newitems = map(lambda item: item[1], items2)
# < items2 is here as we are taking the item[1] from items 2
for item in newitems:
    print(item)

# this can also be written as a list like this
newitems2 = list(map(lambda item: item[1], items2))
print(newitems2)
