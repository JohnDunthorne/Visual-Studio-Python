# to find the index of an item in the list use .index)

letters = ["a", "b", "c"]
print(letters.index("a"))

# this will return 0 as "a" is the first item in the list

# if you want to look up something and your not sure its in the list
# you can run an if statement, this will prevent an error:

# print(letters.index("d")) would error since theres no d in the list but:

if "d" in letters:
    print(letters.index("d"))

# the above will not error since it will only call the print function if "d" is in letters

# you can check to see if there are occurances of an item with the .count method

print(letters.count("b"))
# since theres a "b" in the list this will return 1
