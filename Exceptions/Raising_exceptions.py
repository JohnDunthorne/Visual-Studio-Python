# this is something youll see in peoples code, but is not advisable due to its cost


def calculation(age):
    if age <= 0:
        raise ValueError("age cannot be 0 or less")
    return 10 / age


try:
    calculation(int(input("age: ")))
except ValueError as error:
    print(error)
