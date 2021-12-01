message = input("enter your message: ")
# requires user input: ......
i = 0
# set the value of i at 0, as a variable
word = ""
# sets the word value to nothing
while i < len(message):
    # while i is less than the length of message entered, start of function
    if message[i] == " ":
        # if the message i is equal to space
        print(word)
# print the word
        word = ""
# word again is equal to nothing
    else:
        # otherwise do this
        word = word + message[i]
# word + message i is equal to word
    i = i + 1
# i + 1 is equal to i
print(word)
# print wor
