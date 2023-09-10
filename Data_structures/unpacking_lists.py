numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

# aside from doing the above we can unpack this list with a better method

letters = ["a", "b", "c"]
first_letter, second_letter, third_letter = letters

# we have now created new variables for all the items in the list, just like above

# if you dant want to create varibles for everything in a list, you can unpack some and leave the rest

numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first_number, second_number, *numbers3 = numbers2

print(first_number)
print(second_number)
print(numbers3)

# with this we extracted the first two nnumbers as their own variables
# and used the remainder of the list to create a new list

print(numbers2)
print(numbers3)
# as you can see numbers 2 remains unchaged as we defined a new variable for the remaining list
