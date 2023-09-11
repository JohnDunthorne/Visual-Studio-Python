letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)

    # enumerate returns the index value as well as the object in list

# we can add items to a list:

# with append (adds to the end of the list)
letters.append("d")
print(letters)

# with insert (type the index, then the new item)
letters.insert(2, "-")
print(letters)

# we can remove items with:

# pop (this removes the item from the end of the list)
letters.pop()
print(letters)

# pop(2) (this removes the item in index 2, or whatever number you write in parentheses)
letters.pop(2)
print(letters)

# remove (use this to type the name of a specific item in the list, it will remove the first occurance of it)
letters.remove("c")
