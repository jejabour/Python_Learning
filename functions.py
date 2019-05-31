#This program is an example of how to use a function
#And gives an example of parameters and arguments

#The 'name' inside here is called the parameter of the function
def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard!')


print("Start")

#The names passed from here are called the arguments
#There MUST be an argument passed when the function has parameters
greet_user("John")
greet_user("Mary")

print("Finish")
