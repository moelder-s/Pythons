password = "python123"
i = 0
for i in range (1,4):
    password =(input("Enter Your password: "))
    if password == "python123":
        i = i + 1
        print("Access Granted")
        break
    if i <= 3:
        print("Account blocked")
else:
    print("Re enter password")

print("number of attempts are = ",i)
