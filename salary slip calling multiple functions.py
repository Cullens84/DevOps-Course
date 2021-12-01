
def payslip(name,salary):
    if salary >=3000:
        tax=salary*30/100
    else:
        tax=salary*20/100
    net=salary-tax
    print("name of emplyee:", name)
    print(name,"'s salary is", salary)
    print("tax calculated:", tax)
    print("-----------")
    print("net salary=",net)
    print("-----------")
payslip("james",2000)
payslip("shafeeq",8125000)
