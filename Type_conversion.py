# x = input("x: ")
# this will crate a variable based on user input for x
# print(type(x))
# this will return what type x is
# y = x + 1
# this will error at run as the x input will be a str and y is adding a int to it it

# the correct way to do this would be
x = input("x: ")
y = int(x) + 1  # this type converts the input for x into an integer
print("y = " + str(y))  # this type convert y into a string
print(f"y = {y}")  # this converts both the sum of x and y from an integer to sring

# we can type convert inputs to different things for example
int(x)  # to convert x to an integer
float(x)  # to convert x to float
bool(x)  # to convert x to a boolean
str(x)  # to convert x to a string

# For bool False can be
# "" <empty brackets will return false
# 0 < the number 0
# None < just typing None
# anything else will return True
