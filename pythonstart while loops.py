counter = 0
# setting a variable with a value
while counter < 5:
    # saying while counter value is less than 5 execute the next command
    print("is continuing")
# print statement while the while statement is true (less than 5)
    counter = counter + 1
# setting the counter to add 1 after the print allows the loop to start again
# this loop will continue until the while loop statement is true
# once it has gone through 5 print statements and the counter adds 1 it becomes 5 so the while statement becomes false and stops (indexing starts at zero not 1)
# it will print "its continuing" 4 times then stop
# without the counter = counter +1 statement it will enter an infinate loop

list = []
# creating an empty list
while len(list) < 5:
    # while the length of list is less than 5 execute the next command
    var1 = input("enter your name:")

# creating a temperary variable to store the user input
    if var1 == "harry":

        # if the temperary variable is equal to harry
        list.append(list)

# append the harry inputted by the user to the list
