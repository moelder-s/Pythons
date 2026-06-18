salary = int(input("Enter Your Salary: "))

if salary >= 100000:
    bonus = salary * 0.15
elif 50000 < salary < 99999:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("Bonus =",bonus)
