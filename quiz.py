total = 0
highest = 0
lowest = 100

for i in range(1, 10):
    mark = float(input(f"Enter mark for Quiz {i}: "))
    
    total = total + mark

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

average = total / 8

print("Results")
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
