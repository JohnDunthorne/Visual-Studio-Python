def increment(number, by):
    return number + by


print(increment(2, by=1))

# if there are 2 parameters in a function, it will expect 2 arguments when calling the function, or an error will occur
# default arguments can be used though:


def increment(number, by=1):
    return number + by


print(increment(3))

# ^^ we have given a default value for 'by' here, so we dont need to set the arguement
# when we call the function and it will use the default value for 'by'


def increment(number, by=1):
    return number + by


print(increment(3, 7))

# ^^ with the code unchanged we can still pass another value for 'by' and it will override the default value
