# lists
pets = ["cat", "dog", "fish", "hamster", "rat"]
# square brackets indicate a list, this list is stored in the variable pets- the commas tell python next item in the list
# you can use len to find the length of a list, you can use indexing 0 being position 1, 1 being position 2 etc
# or you can use negative indexing with -1 beinhg the last -2 being the second to last etc
print(len(pets))
# you slice a list, you can get items using indexing, but the specified numbers are from index number to index number spereated by a colon.
# the up to number is not inclusive
print(pets[1:3])  # result of this print is ['dog','fish']
print(pets[0:4])  # result of this print is ['cat', 'dog', 'fish', 'hamster']

pets[1] = "heron"
# this will replace the item at position 1 with heron, index position 1 being position 2 as position 0 is counted as the first

pets.append("giraffe")
# this will append to the end of the list using .append
print(pets)


del pets[0]
# this will delete from the list at the index position stated in square brackets

pets.pop(2)
# this pops an item off your list using the index position

pets.remove("giraffe")
# this removes the item stated and cannot be used with index position
print(pets)
# you can print from a list a true false statement like print("cat" in pets) if its in the list it will print if its not it will print false to the screen
print("giraffe" in pets)
# you can also have a list inside a list. this is called nesting
pets.append(["car", "van", "truck", "bus"])
# here we have appended a list into a list.
print(pets)
# dictionary's
print(len(pets))
