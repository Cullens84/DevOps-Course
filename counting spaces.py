#this logic take input from user can count the words entered 
message = input("enter your message: ")
space = 0
i = 0
#the line below is while the i variable is less than the length of message
while i <len(message):
    if message[i] == " ":
#the below means  it will count spaces or words incrementally from 1
        space=space+1
        i=i+1
print(space)
#print("you have entered", space+1,"words")
#how are we doing this