age = int(input("Enter your Age: "))
citizen = str(input("Are you a citizen (yes/no): "))

if age >= 18:
    if citizen == "yes":
        print("Eligible to vote")
    else:
        print("Not eligible to vote")
else:
    print("Not eligible to vote")
    
