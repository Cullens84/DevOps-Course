def tax(salary):
    if salary>=3000:
        tax=salary*30/100
    else:
        tax=salary*20/100
    return tax

name=input("enter your name: ")
salary=int(input("enter your salary: "))
net=salary-tax(salary)
print("your tax:",tax(salary))
print("net salary:",net)
