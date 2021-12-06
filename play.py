#calculate the amount of cms to pay

#calculation is your gross wage after pension but before deductions

#amount payable is 21% of gross pay post pension but pre deductions


gross_pay = float(input("Please enter your total gross pay:"))
Pension = float(input("please imput your pension contribution:"))
deduction = 0
net_pay = 0
while gross_pay < 0:
    if Pension < 0:
        gross_pay = gross_pay - deduction
    deduction = gross_pay /100 * 21
    net_pay = gross_pay - deduction - Pension
print("your deduction is ", deduction)
print("your pension contribution is",Pension)
print("your gross pay is",gross_pay)
