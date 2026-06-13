roomavailable = str(input("Room available (yes/no): "))

if roomavailable == "yes":
    idnumber = str(input("Do you have a valid ID (yes/no): "))
    if idnumber == "yes":
         payment = str(input("Advaced payment completed (yes/no): "))
         if payment == "yes":
             nights = int(input("Number of nights: "))
             if nights >= 1 :
                 print("Check in Approved")
             else:
                 print("Check in not approved")
         else:
             print("Check in not approved")
    else:
         print("Check in not approved")
else:
    print("Check in not approved")
