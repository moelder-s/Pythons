i = 0

for i in range (1,6):
    units = float(input(f"Customer {i} Units = "))

    if units < 101:
        bill = units * 10
    elif 101 <= units <= 200:
        bill = (100*10) + (units-100)*15
    else:
        bill = (100*10) + (units-100)*15 + (units-200)*20

    print(f"Customer {i} Bill is = ",bill)

    i = i + bill

    
        
