print("SALARY PROGRAM")
name=input("Enter Name Of Employee")
salary=int(input("Enter Basic Salary"))
print()
print("SALARY DETAILS")
print("NAME OF EMPLOYEE :",name)
print("BASIC SALARY :",salary)
DA=(25/100)*salary
HRA=(15/100)*salary
TA=(7.5/100)*salary
TAX=(5/100)*salary
PF=(12/100)*salary
print("DEARNESS ALLOW :",DA)
print("HOUSE RENT ALLOW",HRA)
print("TRAVEL ALLOW",TA)
print()
net_pay=salary+DA+HRA+TA
print("NET SALARY PAY :",net_pay)
print("PROVIDENT FUND:",PF)
print("TAX :",TAX)
gross_pay=net_pay-PF-TAX
print("GROSS PAYMENT :",gross_pay)