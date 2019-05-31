#This program is an example of how to use a function
#And gives an example of parameters and arguments

#The names inside here is called the parameter of the function
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard!')


print("Start")

#The names passed from here are called positional arguments. Order matters
#There MUST be an argument passed when the function has parameters
greet_user("John", "Smith")
greet_user(last_name = "Smith", first_name = "John")

print("Finish")
