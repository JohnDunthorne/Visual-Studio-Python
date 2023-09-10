# you can return specific items in your list by calling thier index number/s

letter = ["a", "b", "c", "d"]
print(letter[0])
print(letter[:])
print(letter[1:3])
print(letter[-1])

# the basic purpose of this is to change an element in the list of instance

letter[0] = "A"

print(letter)

# this changed the lowercase a to an uppercase A

# you can call every other number as well, with a 3rd input:
numbers = list(range(100))
print(numbers[::5])
# in this case we looked up every 5th object from 0 to 100
