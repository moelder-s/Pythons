registered = str(input("Are you registered (yes/no): "))

if registered == "yes":
    fees = str(input("Fees is paid (yes/no): "))
    if fees == "yes":
        print("Approved")
    else:
        print("Rejected")
else:
    print("Rejected")
        
