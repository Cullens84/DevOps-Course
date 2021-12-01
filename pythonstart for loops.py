# for loops use the operator "in"
# the second entry in the for loop statement must be some kind of iterable, list, dict, set
# we use a temperary variable in the statement to store the loop
from typing import cast


list1 = ["cat", "dog", "fish", "cat", "dog", "fish", "cat", "dog", "fish"]
# creating the list with values inside
for i in list1:
    # for i (which is all at the moment) in list1
    if i == "cat":
        # if i is equal to cat execute the next command
        print("i dont like cats!")
    else:
        print(i)
# otherwise print i
# print i, as i has no value, or input into it at all, using i as the temperary variable is standard practice

list2 = []
# creating an empty list
for i in range(5):
    list2.append(input("please enter animal:"))
# this allows you to enter 5 inputs to the empty list with the .append
print(list2)
# range is up to that number but not including it.

#this is range
for i in range(17, 73):
    print(i)
# this means for i(which is the place holder) range from 17 to 73, but does not include 73.
# range allows the loop to iterate over

var1 = "Hello"
var2 = "world"

for i in var1:
    var2 = i + var2
# this will take the variable created(var2) and add i from var1 which is anything so it starts from h and adds var2 world, would look like
# Hworld
# eHworld
# leHworld
# lleHworld
# olleHworld
# it adds each letter of var1 to the full string of var2 one charachter at a time
    print(var2)
# this will take each charachter from the string(var1) and print it individually.

dict1 = {1: "hello", 2: "world"}
# creating a dictionary with key value pairs
for i, j in dict1.items():
    # this means for i , j = there will be pairs of items. i and j are just place holders they can be anything but standard say i then j
    print(i)
    print(j)
# this returns - 1 hello 2 world.
