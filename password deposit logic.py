password = "password123456"

deposit = int(input("enter your deposit: ")) 
password = input("enter your passwrod: ")

if 0 < deposit <= 100:
    print(f"Thank you for the £{deposit} deposit!")
else:
    print("This is not a valid amount to deposit.")
