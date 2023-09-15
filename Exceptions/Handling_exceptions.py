# we are going to deal with the 'ValueError" we incurred from typing something other than an 'int'

try:
    age = int(input("age: "))
except ValueError:
    print("Type numbers only")
    print("an exception was thrown")
else:
    print("no exceptions were thrown")
print("program didnt crash")
