# while loops continue as long as a certain condition is true
x = 1
while x < 10:
    print(x)
    x += 1
# this while loop will continue adding 1 to x until it reaches 10, then will stop printing the result
print("*" * 30)

command = ""
while command.lower() != "quit":
    command = input(">")
    print("echo", command)

# this will expect the input 'quit' to terminate the program, anything else it will echo back to you
# added .lower() DONT FORGET () after .upper() and .lower() etc
# to command so input from user can be quit in upper or lowercase, or a mixture, and not matter.
