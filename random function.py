def printReverse(msg):

    word = " "
    i = len(msg)-1
    while i >= 0:
        if msg[i] == " ":
            print(word)
            word=""
        else:
            word=msg[i]+word

    i-=1
    print(word)

printReverse("I am back")
printReverse("We are learning python")