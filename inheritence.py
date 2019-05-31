#This will be an example of classes inheriting code from other parent classes

# Mammal class is acting as a parent class with a method
# That will be used in the dog and cat classes
class Mammal:
    def walk(self):
        print("walk")

# The mammal in parenthesis allows Dog to get the methods used in Mammal
# The pass is there so python doesn't freak out by having an empty class
# Just means to pass over that line
class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()