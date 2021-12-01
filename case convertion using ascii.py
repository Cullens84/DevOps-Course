def uppercase(msg):
    newmsg = ""
    i = 0
    while i < len(msg):
        if ord(msg[i]) >= 97 and ord(msg[i]) <= 122:
            newmsg += chr(ord(msg[i])+-32)
        else:
            newmsg += msg[i]
        i += 1
    print(newmsg)


uppercase("Hello My FRIENDS")
# this is the logic behind converting case using ascii codes
