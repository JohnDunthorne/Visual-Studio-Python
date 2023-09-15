# if we open a file we have to close it

try:
    file = open("Exceptions.py")  # < we opened a file here
    age = int(input("age: "))
    calculation = 10 / age
except (ValueError, ZeroDivisionError):
    print("not a valid input")
    print("an exception was thrown")
else:
    print("no exceptions were thrown")
finally:  # < the finally clause will execute nomatter the outcome of the try
    file.close()  # < and here we closed our file
