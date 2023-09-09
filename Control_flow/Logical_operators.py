# the three logical operators in python are "and" "or" and "not"

high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")
# this one will return not eligible, since both need to be 'True'
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")
# this one will return eligible, since one of the two conditions are 'True'

student = True
if student:
    print("Eligible")
elif not student:
    print("Ineligible")
# if student was marked False, this would return Ineligible

if (high_income or good_credit) and student:
    print("Eligible")
else:
    print("Ineligible")
# this would return Eligible, since one of the first two conditions is 'True', and student is 'True'
