Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> room_charge=float(input("enter room charge per day:"))                          days=int(input("Enter number of days:"))                                        food_charges=float(input("Enter food charges:"))                                service_percentage=float(input("Enter service charge percentage:"))             subtotal=(room_charge*days)+food_charges                                        service_charge=subtotal*(service_percentage/100)                                final_bill=subtotal+service_charge
SyntaxError: invalid syntax
>>> print("subtotal=",subtotal)                                                      print("service Charge=",service_charge)                                         print("final bill=",final_bill)
SyntaxError: invalid syntax
