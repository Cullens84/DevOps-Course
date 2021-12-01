var1 = input("Enter your texte here:")
# this is setting up a variable (var1) and storing inside of it the users entry as denoted by the : inside the brackets
var2 = var1.upper()
var3 = var2.lower()
# this creates a new variable (var2) and is using a built in
# function .upper or .lower to make the string stored in var1 uppercase in var2
var4 = var1.replace("a", "there was an a here")
# this creates a new variable (var4) with the built in function .replace
# this replaces what is specified in the brackets .replace("what you want replaceing", "what to replace it with")
var5 = var4.split("w")
# creating var5 and using .split on var for to populate it.
# .split defaults to a space if no argument is passed in the brackets
# it removes the space and splits the string up, if a letter is passed in this example
# it will remove it, use a space and split the contextr into individual words.
print(var1)
# prints to the screen var1
print(var2)
# prints to the screen var2
print(var3)
# prints to the screen var3
print(var4)
# prints to the screen var4
print(var5)
