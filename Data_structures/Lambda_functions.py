items = [
    ("product3", 30),
    ("product1", 10),
    ("product2", 20),
    ("product5", 50),
    ("product4", 40),
]
print(items)


def sort_item(item):  # < (item) is the parameter for lambda
    return item[1]  # < item[1] is the expression for lambda


items.sort(key=sort_item)
print(items)

# you can use lambda to prevent you from needing to define a function if youre only going to use it once
# in the below case we have removed the defines function altogether and used lambda instead.
items2 = [
    ("product3", 31),
    ("product1", 12),
    ("product2", 23),
    ("product5", 54),
    ("product4", 45),
]
items2.sort(key=lambda item: item[1])  # follow key = with parameters:expression
print(items2)
