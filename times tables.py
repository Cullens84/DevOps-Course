num = int(input('enter the multiplication table you wish to view: '))
length = int(input('enter the number you wish to multiply up to: '))
for i in range (length+1):
    print(num, "x", i, "=", num*i)
import time
startTime = time.time()
# write your code or functions calls
endTime = time.time()
totalTime = endTime - startTime

print("Total time required to execute code is= ", totalTime)