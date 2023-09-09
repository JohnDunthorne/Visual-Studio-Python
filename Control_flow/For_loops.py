print("sending a message")
print("sending a message")
print("sending a message")
# this is ugly code, to repeat a task use a 'for' loop

for number in range(3):  # we are passing 3 as an argument
    print("Attempt", number)
# number will return each attempt index, in this instance 0, 1 and 2

# to make this more user friendly we can write like this:
for number in range(3):
    print("Attempt", number + 1)
# which will return attempts as 1, 2 and 3

# to avoid this we could also write
for number in range(1, 4):
    print("Attempt", number, number * ".")
# this ultimately returns the same result without having to type number + 1
# also added number * "." to add that many dots after statement. just for fun

for number in range(1, 20, 3):
    print("Attempt", number, number * ".")
# when dealing with ranges you can specify a step as well (3rd number in brackets), in this case
# it will list numbers between 1 and 19 (the 1, 20 in the brackets), but only every third
