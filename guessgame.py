import random

num = random.randrange(1, 10)
print(num)

guess_count = 0
guess_limit = 3


while guess_count < guess_limit:
    guess = int(input("Make a guess 1-10: "))
    
    guess_count += 1

    if guess == num:
        print("You guessed correctly!")
        break
    else:
        print("Sorry! That wasn't right.")
        print(f"You have {guess_limit - guess_count} tries left")
else:
    print("You lost!")