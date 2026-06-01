weight = float(input("Enter Your Weight(kg):"))
height = float(input("Enter Your Height(m):"))

bmi = weight / (height ** 2)

print("BMI =",round(bmi,2))

if 0<bmi<18.5:
    print("Underweight")
elif 18.5<bmi<24.9:
    print("Normal weight")
elif 25.0<BMI<29.9:
    print("Overweight")
else:
    print("Obese")
