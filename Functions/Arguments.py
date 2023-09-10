def greet(first_name, last_name):
    # first_name, last_name are considered parameters, not arguements.
    print(f"hi {first_name} {last_name}")
    print("welcome aboard")


# above we are expecting 2 arguements for first and last name, we will put these in below when calling the function.
greet("John", "Dunthorne")

# defining your own functions can be useful, in this case
# we can greet multiple people without writing all that print code

greet("Brittany", "Duman")
greet("Fallon", "Dunthorne")
