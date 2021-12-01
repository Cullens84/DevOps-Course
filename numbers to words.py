def teenprefix(no):
    answer = ""
    if no == 20:
        answer = "twenty"
    if no == 30:
        answer = "thirty"
    if no == 40:
        answer = "forty"
    if no == 50:
        answer = "fifty"
    if no == 60:
        answer = "sixty"
    if no == 70:
        answer = "seventy"
    if no == 80:
        answer = "eighty"
    if no == 90:
        answer = "ninty"
    return answer
# this first function teenprefix assigns the teen prefix appropriate for the entered numeber


def ones(no):
    answer = ""
    if no == 1:
        answer = "one"
    elif no == 2:
        answer = "two"
    elif no == 3:
        answer = "three"
    elif no == 4:
        answer = "four"
    elif no == 5:
        answer = "five"
    elif no == 6:
        answer = "six"
    elif no == 7:
        answer = "seven"
    elif no == 8:
        answer = "eight"
    elif no == 9:
        answer = "nine"
    elif no == 10:
        answer = "ten"
    elif no == 11:
        answer = "eleven"
    elif no == 12:
        answer = "twelve"
    elif no == 13:
        answer = "thirteen"
    elif no == 14:
        answer = "fourteen"
    elif no == 15:
        answer = "fifteen"
    elif no == 16:
        answer = "sixteen"
    elif no == 17:
        answer = "seventeen"
    elif no == 18:
        answer = "eighteen"
    elif no == 19:
        answer = "nineteen"
    elif no == 0:
        answer = "zero"
    return answer
# this converts the entered number to function called ones to the associating word applicable in the given list


num = int(input("enter any number:"))
result = ""
if num >= 1000:
    result = ones(int(num/1000)) + " thousand "
    num %= 1000
if num >= 100:
    result += ones(int(num/100)) + " hundred "
    num %= 100
if num >= 20:
    result += teenprefix(int(num/10)*10) + " "
    num %= 10
if num >= 1:
    result += ones(num) + " "
# this ensures the functions cycle through appropriately assigning thousand, hundred so on
print(result)
# prints the result
