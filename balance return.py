bill = int(input("enter the amount:"))
paid = int(input("enter the amount paid:"))
balance = paid-bill
if balance >= 50:
    n = int(balance/50)
    balance = balance-(n*50)
    print("£50=", n)
if balance >= 20:
    n = int(balance/20)
    balance = balance-(n*20)
    print("£20=", n)
if balance >= 50:
    n = int(balance/10)
    balance = balance-(n*10)
    print("£10=", n)
if balance >= 5:
    n = int(balance/5)
    balance = balance-(n*5)
    print("£5=", n)
if balance >= 2:
    n = int(balance/2)
    balance = balance-(n*2)
    print("£2=", n)
if balance >= 1:
    n = int(balance/1)
    balance = balance-(n*1)
    print("£1=", n)