statement = input("Enter a statement: ")
vowels = 'aeiouAEIOU'
count = 0
for char in statement:
    if char in vowels:
        count += 1
if count == 0:
    print("No vowels found")
else:
    print("Number of vowels:", count)
