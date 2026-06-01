basic_salary = float(input("Enter basic salary: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate: "))
bonus = float(input("Enter bonus: "))
tax_percentage = float(input("Enter tax percentage: "))

overtime_pay = overtime_hours * overtime_rate
gross_salary = basic_salary + overtime_pay + bonus
tax = gross_salary * (tax_percentage) / 100
net_salary = gross_salary - tax

print("Gross salary is =", gross_salary)
print("tax is =", tax)
print("net salary =", net_salary)
