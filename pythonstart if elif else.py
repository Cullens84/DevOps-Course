var1 = int(input("Please enter a number:"))
# creating a variable from the user input, and setting it as an integer(whole number)
if var1 < 10 and var1 < 5:
    # the or will use var1 on both sides and compare using the greater than or less than operators <> to assess the command
    # you can use the and operator to extend the command, but the and operator must be true on both sides of "and" for the command to work
    print("less than 10 and less than 5")
elif var1 < 10:
    print("less than 10 but greater than 5")
else:
    print("greater than 10")
# otherwise execute the next command
# this statement is saying if it is if the users input is less than 10 print "less than 10"
# otherwise print "is equal to or greater than"
# start with an "if" staement, followed by "elif" and ending on an "else" statement
# you can use as many elif statements as you want


var2 = int(input("Please Enter your marks:"))
# here we create another variable from a user input
if var2 >= 85:
    print("Distinction")
# if the mark is greater than or equal to print distinction
elif var2 < 85 and var2 >= 65:
    print("Pass")
# else if the mark is less than 85 but greaterthan or equal to 65 print pass
else var2 < 65:
    print("Fail")
# else mark entered is less than 65 print fail
