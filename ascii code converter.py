
alpha = input("enter any alphabet: ")
# this takes your input as a user and assigns it to alpha
if ord(alpha) >= 65 and ord(alpha) <= 90:
    print("you have entered a uppercase letter")
# this takes your input alpha and compares it to the ascii range for uppercase
elif ord(alpha) >= 97 and ord(alpha) <= 122:
    print("you have entered a lowercase letter")
# this takes your input alpha and compares it to the ascii range for lowercase
elif ord(alpha) >= 48 and ord(alpha) <= 57:
    print("you have entered a digit")
# this takes your input alpha and compares it to the ascii range for digits
elif ord(alpha) >= 33 and ord(alpha) <= 47:
    print("you have entered a special charachter")
elif ord(alpha) >= 58 and ord(alpha) <= 63:
    print("you have entered a special charachter")
elif ord(alpha) >= 91 and ord(alpha) <= 96:
    print("you have entered a special charachter")
elif ord(alpha) >= 123 and ord(alpha) <= 126:
    print("you have entered a special charachter")
    # this takes your input alpha and compares it to the ascii range for special charachters()
