i = 0
Eligible = 0
NotEligible = 0

for i in range (1,11):
    att = int(input(f"Enter No{i} student attendance percentage = "))

    if att >= 75:
        Eligible = Eligible + 1
    else:
        NotEligible = NotEligible + 1

    
        avr = (Eligible/10)*100
        
print("Number of students eligible for the exam is =",Eligible)
print("Number of students not eligible for the exam is =",NotEligible)
print("Average attendance of the class is =",avr)

    
