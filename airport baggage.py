weight = float(input("Enter baggage weight (kg): "))

if weight <= 20:
    print("No extra charge")
elif weight <= 30:
    charge = (weight - 20) * 200
    print("Extra charge = Rs.", charge)
else:
    print("Baggage is not allowed")
