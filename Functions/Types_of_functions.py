# there are 2 types of functions you can define
# 1 - Perform a task
# 2 - Return a value


def greet(name):
    print(f"Hi {name}")


greet("John")

# greet and print functions are examples of type #1 they perform a task

round(2.8)

# the round function is an example of #2, it returns a value, in this case the number 3


def get_greeting(name):
    return f"hello {name}"


# using return vs print, we just have a value returned to memory that we can use later
# for example

message = get_greeting("John")
print(message)

# we are not tied to printing it right away in the scenario, its just saved for later in the 'message' variable
