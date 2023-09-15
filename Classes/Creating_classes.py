# we use a different naming convention for classes
# we dont separate words with an underscore, and the first letter of each word
# should be capitalized
# for instance **ThisIsMyClass** would work


class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
