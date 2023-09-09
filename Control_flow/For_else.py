successful = True
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("unsuccessful")


# in this for loop if successful in attempt it will print 'successful' the end (break) the rest of the loop
# if all 3 attempts are made, and stull does not work, the else stament will kick in
# you will see all 3 attempts and then 'unsuccessful' written at the end
