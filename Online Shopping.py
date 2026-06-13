loggedin = str(input("Are you logged in (yes/no): "))

if loggedin == "yes":
     cartvalue = int(input("Enter cart value: "))
     if cartvalue > 1000:
         payment = str(input("Payment succesfull (yes/no): "))
         if payment == "yes":
             print("Order Confirmed")
         else:
             print("Order not Confirmed")
     else:
         print("Order not Confirmed")
else:
    print("Order not Confirmed")
        
