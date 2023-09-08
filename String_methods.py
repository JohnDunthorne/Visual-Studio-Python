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
