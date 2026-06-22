total = 0
i = 0

for i in range (1,25):
    bill = int(input("Enter your item price  = "))
    if bill == 0:
        break
    if bill > 0:
        total = total + bill
       
i = i + 1
print("Your total bill is =",total)       
print("No of items are =",i)
