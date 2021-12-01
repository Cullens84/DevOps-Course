var1 = "hello"
var2 = "world"
var3 = var1 + " " + var2

print(var3)
# creating three variables, assigning var1 and var2 values ("hello" and "world") and adding var1 and var2 together as shown is acceptable in python.
# this is concatenation, adding strings together

print("Hello" + " " + "World")
print("Hello", "World")
# these two print statements return the same result as the comma in the second statement wont be printed as a comma but as a space insead.

print(f"Hello World")
# the point of using the f prefix is to format the following string
print(f"{var1} {var2}")
# this is passing two variables into the f string using curly brackets, this is cleaner and simpler to understand.
# you can add text into the fstring and it will be printed as follows
print(f"{var1} {var2}""hello world")

print(f"{var1} \n{var2}")
# you can use a backslash and an escape character to do things like \n is new line, \t is a tab, \u is unicode for smiley faces and emoji's.
print(f"{var1} \t{var2}")
print(f"{var1} \U0001f600{var2}")
