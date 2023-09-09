temperature = 15
if temperature > 30:
    print("its kinda hot out")
elif temperature > 20:
    print("its kinda cool out")
else:
    print("its cold out today")
print("Done")
# this particular statement will return "its cold" since the first two staments are not true, it will skip to the else stament
# the "done" string will appear regardless of any of the staments as it is at the bottom and not indented, it will run nomatter the outcome
