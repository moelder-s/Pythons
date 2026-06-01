num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

if num3>num2 and num3>num1:
    print("The largerst number is :", num3)
elif num1>num3 and num1>num2:
    print("The largest number is :", num1)
else:
    print("The largest number is :", num2)
