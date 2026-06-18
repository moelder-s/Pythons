#Q4
total = 0

for i in range(10):
    mark = int(input("Enter mark: "))
    total = total + mark

average = total/10

print("Total =",total)
print("Average =",average)

if average < 50:
    print("Fail!")
else:
    print("Pass!")

#Q5
total = 0

num = int(input("Enter number (enter-1to stop): "))

while num != -1:
     total += num
     num = int(input("Enter number (enter-1to stop): "))
print("Total :",total)

#Q6
text = input("Enter a Text: ")

count = 0
i = 0

while i < len(text):
    if text[i] == 'a' or text[i] == 'e' or text[i] == 'i' or text[i] == 'o' or text[i] == 'u':
        count = count + 1
    i = i + 1

print("Number of vowels =",count)
        
    

     
    
