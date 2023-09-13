# dictionaries are a collection of key value pairs, like a phone book
# the pair being:
# name -> number

# we can use the dict function to create this dictionary with keyword arguements

dictionary = dict(john=5556789, brittany=5554315, fallon=5674829)
# we can now access any of these by passing the index
print(dictionary["john"])
print(dictionary)

# you can add key values
dictionary["mackenzie"] = 3456789
print(dictionary)

# if you try to print an item that doesnt exist youll get an error, so do this:
if "douglas" in dictionary:
    print("douglas")
# douglas will only print if it exists in the dictionary

# you can also use the get method

print(dictionary.get("douglas"))
# this will return "None" if its not in the list (by default)
print(dictionary.get("douglas", 0))
# you can also pass a second arguement to have it return something of your choosing (a '0' in this instance)
print(dictionary.get("john"))

# you can delete items in a dictionary

del dictionary["john"]
print(dictionary)

# you can also loop over dictionaries
for key, value in dictionary.items():
    print(key, value)
# this returns
# brittany 5554315
# fallon 5674829
# mackenzie 3456789
