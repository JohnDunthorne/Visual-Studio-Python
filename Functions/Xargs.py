def multiply(x, y):
    return x * y


print(multiply(2, 3))

# with this method we can only multiply 2 number together, x and y


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# we create an object called totals, which is what out multiply function will return eventually
# for number in numbers, we will take the total, and multiply by the first number
# total *= number, will take that multiplication and update the number for total
# in this case it will take total(1) and times it by number in numbers (2) and return 2
# total is now updated and is (2)
# the loop will continue and take new total (2) and multiply bu the next number (3) and so on
# once all numbers are addressed the function will return total, so when we print(multiply(x, x, x, x))
# it returns total

print(multiply(2, 5))
print(multiply(3, 4, 5, 6))
