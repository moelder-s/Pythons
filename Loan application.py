salary = int(input("Monthly salary: "))

if salary > 50000:
    creditscore = int(input("Enter Credit score: "))
    if creditscore > 700:
        print("Loan Approved")
    else:
        print("Loan Rejected")
else:
    print("Loan Rejected")
