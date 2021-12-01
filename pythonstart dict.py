dict1 = {1: "james", 2: "paul", 3: "peter", 4: "harry"}

# dictionaries are denoted by curly brackets and are key value pairs, key being just that and the pair being the data
# the key can be anything you want, the key is the stated index for that entry
print(dict1)

dict1[1] = "larry"
# replacing the key value of 1 with larry
dict1[5] = "mike"
# here because key 5 doesnt exist and we have given the value "mike" it will just add it to the list
print(dict1)

print(dict1.keys())
# this dot method allows you to just print out the keys for the dictionary stated.
print(dict1.values())
# same principle you can just print out the values
print(dict1.items())
# this prints out the key value pair coupled together in bracket
# the print would look like
#dict_items([(1, 'larry'), (2, 'paul'), (3, 'peter'), (4, 'harry'), (5, 'mike')])
# dictionaries have to be key value pairs the keys can be anything
# the key value pair must be split up by a colon.


