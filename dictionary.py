#This program asks the user for a phone number
#It will then repeat the numbers back alphabetically

phone = input("Please enter your phone number")

#We map ech digit to the alphabetical equivalent
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

#We create an empty string to fill with the inputs
output = ""

for ch in phone:
    #This takes the mapping of the digits from phone and puts them into the string
    #The ! is in case a character not in the dictionary is used
    output += digits_mapping.get(ch, "!") + " "

print(output)

