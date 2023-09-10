# this while loop will go on forever until 'if' command is met and program 'break' is triggered.

while True:
    command = input(">")
    print("echo", command)
    if command.lower() == "quit":
        break
