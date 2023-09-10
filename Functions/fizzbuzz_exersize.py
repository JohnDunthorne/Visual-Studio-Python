# if number is divisible by 3, return fizz
# if number is divisible by 5, return buzz
# if number is divisible by both, return fizzbuzz
# otherwise return the input


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    elif input % 5 == 0:
        return "buzz"
    elif input % 3 == 0:
        return "fizz"
    else:
        return input


print(fizz_buzz(2))
