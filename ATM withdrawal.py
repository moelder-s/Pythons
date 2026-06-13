balance = 20000

pin = int(input("Enter your pin: "))

if pin == 1234:
    withdrawal = int(input("Enter your withdrawal: "))
    if withdrawal < 20000:
        print("You can withdraw Your money")
    else:
        print("Your minimum balance is 20000")
else:
    print("Incorrect password")
