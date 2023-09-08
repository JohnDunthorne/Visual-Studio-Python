# a function is a reusable piece of code that performs a task
# len is a function that returns the length of a string - for example
course_name = "learn python in 0.45 seconds for real dawg, you can do it"
print(course_name)
number_or_characters = len(course_name)
print(f"the phrase '{course_name}' has {number_or_characters} characters in it")
# another example of using f string to call up variables

# we can call up a particular part of a sting using [] square brackets and inserting an index value
print(course_name[0])
# remember that [0] is the first character in the string , not [1] which would be the second
print(course_name[-1])
# negative indexes start from the end of the string and work backwards
print(course_name[0:3])
# this will return the first 3 characters in the string (the 0 the 1 and the 2) not the 3 as well
print(course_name[0:])
# leaving the second field empty will return everything past the first index
print(course_name[3:])
# this will return everything from index 3 to the end
