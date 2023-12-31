letters = ["a", "b", "c"]

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
print(letters)

# del can be used to delete an item by index, or a range of items:
del letters[1]
print(letters)

letters = ["a", "b", "c", "d", "e", "f"]
del letters[0:3]
print(letters)

# clear deletes all items in a list
letters.clear()
print(letters)
