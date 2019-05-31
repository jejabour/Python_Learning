import random

for i in range(5):

    # This prints values between 0 and 1
    # print(random.random())

    #This prints integers between 10 and 20
    print(random.randint(10, 20))

#This picks a random from a list
members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)
