mark = int(input("Enter student mark: "))

if mark >= 75:
    income = int(input("Enter student family income: "))
    if income < 50000:
        print("Approved")
    else:
        print("Rejected")
else:
    print("Rejected")


