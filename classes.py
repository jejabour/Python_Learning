#This program will be an example of classes

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


#Creates a Point object, so now this variable has the move and draw characteristics
#An object is an instance of a class. The class has the blueprints of the object
point1 = Point()

#The def methods have attributes that you can make and use
point1.x = 10
point1.y = 20

print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)