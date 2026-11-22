#Electricity Billing System 
def calculatebill(n):
    if n<=100:
        bill=n*1.50
    elif n<=200:
        bill=(100*1.50)+(n-100)*2.50
    elif n<=500:
        bill=(100*1.50)+(100*2.50)+(n-200)*4.00
    else:
        bill=(100*1.50)+(100*2.50)+(300*4.00)+(n-500)*6.00
    return bill
n=int(input("Enter number of Customers :"))
for i in range(1,n+1):
    name=input("Enter your Name :")
    print(f"Customer {i} ")
    units=float(input(f"Enter Units Consumed :"))
    bill=calculatebill(units)
    print("Customer Name :",name)
    print("Units     :",units)
    print("Bill Amount  :Rs.",round(bill,2))
    