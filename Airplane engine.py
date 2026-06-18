#Q2
safe = 0
maintan = 0
engine = 1

while engine <= 4:
    temp = float(input("Enter temperature: "))
    if 200 <= temp <= 850:
        print("Engine",engine,"Safe")
        safe = safe + 1
    else:
        print("Engine",engine,"Maintanance required")
        maintan = maintan + 1

    engine = engine + 1

print("Engine Safe = ",safe)
print("Maintanance Required = ",maintan)

#Q3
num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial = factorial * i
    i = i + 1

print("Factorial is = ",factorial)


