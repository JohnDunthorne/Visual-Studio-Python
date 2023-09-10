x = 1
y = 2
z = 3
a = 4
unit_price = 5
print(x, y, z)

for x in range(2, 10, 2):
    print(x)
print("there are 4 numbers")

count = 0
for y in range(1, 10):
    if y % 2 == 0:
        # ^^ this just means if the remainer of y i zero after being divided by 2 (odd numbers wont be zero)
        count += 1
        print(y)
print(f"there are {count} even numbers")
