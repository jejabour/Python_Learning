#This program is going to be an example to deal with errors

#This is an example of: ValueError: invalid literal for int() with base 10
#Enter letters instead of numbers here

# age = int(input('Age: '))
# print(age)


#To fix:
# try:
#     age = int(input('Age: '))
#     print(age)
# except ValueError:
#     print('Invalid value')





#Example of :ZeroDivisionError
#Enter 0 for the age
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income / age
#     print(age)

# except ValueError:
#     print('Invalid value')


#To fix
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)

except ZeroDivisionError:
    print('Age cannot be 0.')

except ValueError:
    print('Invalid value')
