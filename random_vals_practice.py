# The challenge here was to make a program that will print
# a dice roll, two random numbers b/w 1 and 6, but 
# to do it in a class and as a tuple

import random

class Dice:
    def roll(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        #apparently python will return a tuple even if you don't inlcude ()
        return (die1, die2)


die = Dice()
print(die.roll())