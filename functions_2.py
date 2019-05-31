#This program is an example of functions that return values

def square(number):
    return number * number
    #functions will by default return None if you don't specify


num = int(input("Please provide a number to be squared: "))

print (square(num))