age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# a cleaner way to write this code is to make the if statements variables, and just print the variable at the end

age = 16
if age >= 18:
    message = "Eligible"
else:
    message = "Ineligible"
print(message)

# even cleaner is this

age = 50
message = "Eligible" if age >= 18 else "Ineligible"
print(message)
