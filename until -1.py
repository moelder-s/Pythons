#Q6
text = input("Enter a Text: ")

count = 0
i = 0

while i < len(text):
    if text[i] == 'a' or text[i] == 'e' or text[i] == 'i' or text[i] == 'o' or text[i] == 'u':
        count = count + 1
    i = i + 1

print("Number of vowels =",count)
