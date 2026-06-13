hum = float(input("Enter Humidility: "))
temp = float(input("Enter Temperature: "))

if hum > 80:
    if temp > 30:
        ws = float(input("Enter Wind speed: "))
        if ws > 40:
            print("Severe storm Warning: ")
        else:
            print("Heavy rain Expected")
    else:
        print("Cloudy Weather")
else:
   if temp > 35:
       print("Heat Wave Alert")
   else:
       print("Normal Weather")
