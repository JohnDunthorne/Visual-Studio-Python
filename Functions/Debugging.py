def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total  # < this has been indented on purpose to return the wrong total, it should be level with for statment


print(multiply(2, 3, 4, 5, 6))

# when debugging press f9 to create a break point (a place to start testing your code)
# press f10 to test your code line by line
# to step into a function press f11, to watch the loop and see if you can adress the issue
