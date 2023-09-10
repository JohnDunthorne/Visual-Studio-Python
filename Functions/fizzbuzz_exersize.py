# if number is divisible by 3, return fizz
# if number is divisible by 5, return buzz
# if number is divisible by both, return fizzbuzz
# otherwise return the input


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzbuzz"
    if input % 5 == 0:
        return "buzz"
    if input % 3 == 0:
        return "fizz"
    return input


print(fizz_buzz(30))
