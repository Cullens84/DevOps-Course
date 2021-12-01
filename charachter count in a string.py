
msg=input("put your message here: ")
#this takes your input and assigns it to msg
i=0
#this sets the count for i to 0
alpha=[0]*26

while i<len(msg):
    alpha[ord(msg[i])-65]+=1
    i+=1
#while count starts at zero take the string at count zero minus 65 ord assigns teh ascii, plus 1
i=0
#resets the count to zero for i
while i<len(alpha):
    if alpha[i]!=0:
        print(chr(i + 65),"->", alpha[i])
    i+=1
