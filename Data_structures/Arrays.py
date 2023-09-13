# arrays need only be used on large lists that cause performance issues, otherwise just use lists and tuples

# to use arrays you need to import the module
from array import array

# ^ the first array is the module, the second is the class, they just have the same name in this case

numbers = array("i", [1, 2, 3])
# the first parameter is typecode, you can google all the typecodes you can use in arrays
# we are using "i" here, which is a signed integer

# you can use alot of the same methods with arrays as you do with lists
# see "adding_and_deleting section"
# these are things like .append .pop .remove .insert etc.

# in an array the list has to be a certain type (in this isntance it was a signed integer)
# so modifying it with a float will cause an error
numbers[0] = 1.2
# this will return an error as we are trying to change index [0] in numbers to a float (1.2)
