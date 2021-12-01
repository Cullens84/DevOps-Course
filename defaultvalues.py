Name = input("enter your name here:")
Employeeid = input("enter your employee id here:")
Salary = input("enter your salary here:")
Taxrate = input("enter the rate of tax:")



def tax(Salary,Taxrate):
    mytax=Salary*Taxrate/100
    net=Salary-mytax
    print(Name,"-",Employeeid)
    print("---------")
    print("your tax rate is:", Taxrate)
    print("your actual tax amount is:", mytax)
    print("your net salary is:", Salary)


#this stores the default value at the definition stage, but if you 
#call with the right entries for the function it will use your call values instead