command = ""
started = False

print('''
Welcome to the car game! Type 'help' to see a list of commands''')

while True:
    command = str.lower(input())
    if command == "help":
        print('''Type "Start" to start the car.
Type "Stop" to stop the car.
Type "Quit" to exit the game.''')

    elif command == "start":
        
        if started:
            print("The car is already started!")

        else:
            print("The car started!")
            started = True
    elif command == "stop":
        
        if not started:
            print("The car is already stopped!")

        else:
            print("The car has stopped.")
            started = False

    elif command == "quit":
        print("Sorry to see you go.")
        break
    else:
        print("Sorry, I didn't catch that.")
    