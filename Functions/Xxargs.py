# we can use ** for **args to package multiple pieces of data in a function


def save_user(**user):
    print(user)
    print(user["id"])
    print(user["name"])
    print(user["age"])


save_user(id=3, name="John", age=22)

# this creates a dictionary
