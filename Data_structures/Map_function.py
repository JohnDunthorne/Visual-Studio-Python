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
