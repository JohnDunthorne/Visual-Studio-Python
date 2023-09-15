# we will try something different here (from the cleaning up file)

try:
    with open("Exceptions.py") as file:
        print("file opened")
    age = int(input("age: "))
    calculation = 10 / age
except (ValueError, ZeroDivisionError):
    print("not a valid input")
    print("an exception was thrown")
else:
    print("no exceptions were thrown")
