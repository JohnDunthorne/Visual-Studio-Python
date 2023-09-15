# you can add pretty printing
from pprint import pprint

sentence = "This is a common interview question"
# find the most repeated letter in this text

char_frequency = {}  # < dictionary
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

pprint(char_frequency, width=1)  # pprint is a good way to print dictionaries


# ***** i dont fully understand this, i will return to it later when i have more context *****
