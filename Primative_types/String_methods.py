# methods present themselves when putting the symbol '.' after a variable name, they do various things

name = "John Dunthorne"
print(name.upper())
# this will change all the letters to upper case, good for use when requesting inputs from users
name_upper = name.upper()
print(name_upper)
# this is a way to svae the uppercase version as a new variable to use
name_lower = name.lower()
print(name_lower)
# this is identical to upper but produces lower case letters instead

name2 = "john dunthorne"
print(name2.title())
# title will add uppercase to the beginning of each word in the string

name3 = "    john dunthorne   "
print(name3)
print(name3.strip())  # removes white space from the beginning and end of the string
print(name3.lstrip())  # removes white space from the left of the string
print(name3.rstrip())  # Removes white space formt he right of the string

print(name3.find("dun"))
# this will reurn an index number from where the characters i put here start, so "dun" starts at index 9, this is case sensitive

print(name3.replace("j", "r"))
# this will replace the first letter type with the second letter typed

print("john" in name3)
# this returns a boolean as to whether or not the text type here is contained within the variable typed after, i.e. is "john" in the name3 variable

print("john" not in name3)
# this is like the above only is asking if this text is NOT in the variable
