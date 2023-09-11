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
