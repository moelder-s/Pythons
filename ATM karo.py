
total_w = 0
bal = 50000
no_of_sw = 0

print("remaining balance is 50000")
while bal > 0:
    amt = int(input("Enter Your Withdraw amount = "))
    if amt == -1:
        break      
    if bal >= amt:
        bal = bal - amt
        no_of_sw = no_of_sw + 1
        total_w = total_w + amt
        print("remaining balance is = ",bal)
    else:
         print("Insufficient Balance")
              
print("Total Amount Withdrawn =",total_w)
print("Number of succesful withdrawals =",no_of_sw)
        


