# This is very similar to classes.py, but will have constructors

class Point:

    # This method is the constructor, used to construct n object
    # self is used to refer to the object itself.
    # So I think it's saying "Hey I want my x attribute to be equal
    # to whatever is passed in in the first parameter"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# The arguments passed here will be passed into
# the x and y parameters of the constructor
point = Point(10, 20)
print(point.x)

point.x = 11
print(point.x)