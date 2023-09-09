# nested loops are loops inside other loops
for x in range(1, 4):
    for y in range(1, 4):
        for z in range(1, 4):
            for alpha in range(1, 4):
                print(f" ({x}, {y}, {z}, {alpha})")

# this loop will run first inerations of x y z alpha, then continue with alpha until all loops are complete
# then will go to z, and run though alpha again
# will work its way back though y and then x until all coordinates are printed
