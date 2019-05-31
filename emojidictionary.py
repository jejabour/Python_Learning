message = input(">")

#This will let python know to separate characters by a space
words = message.split(" ")

emojis = {
    ':)': '😊 ',
    ':(': '🙁 ',
    ':P': '😛 ',
    ';P': '😜 ',
    ';)': '😉 '
}

output = ""

#This will check the dict for a word to replace it with.
#If not in there, the second value says to just use instead
for word in words:
    output += emojis.get(word, word) + " "

print(output)