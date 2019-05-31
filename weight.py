weight = input("Please enter your numeric weight: ")

unit = input("Did you enter pounds (l) or kilograms (k)? ")

if unit.lower() == "l":
    new_weight = int(weight) / 2.205
    print(f"You are about {round(new_weight)} kilos.")

elif unit.lower() == "k":
    new_weight = int(weight) * 2.205
    print(f"You are about {round(new_weight)} pounds.")

else:
    print("The unit entered was not understood")