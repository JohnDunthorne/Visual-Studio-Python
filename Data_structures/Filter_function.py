# we want to create a filter that returns numbers only 30 or more in price

items = [
    ("product3", 30),
    ("product1", 10),
    ("product2", 20),
    ("product5", 50),
    ("product4", 40),
]
# we could do it like this:
filtered = []
for item in items:
    if item[1] >= 30:
        print(item)

# but there is a built in filter function
price_30_or_above = filter(lambda item: item[1] >= 30, items)
print(price_30_or_above)
# this code does exactly what we did above without the for loop

# we can put them straight in a list too
price_30_or_above = list(filter(lambda item: item[1] >= 30, items))
print(price_30_or_above)
