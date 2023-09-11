def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)

# since we only use the 'result' variable once, theres no point in having it

print(increment(2, 1))
# this is much cleaner if we are only calling this once

# keyword arguments can come in handy here, since we may not be able to see what
# the parameters are 'increment' are, we can write the keyword in, to make the code more readable

print(increment(2, by=1))
# this produces the same result, but the code is more user friendly to read
