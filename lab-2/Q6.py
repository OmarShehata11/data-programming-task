odd_sum = 0
even_sum = 0
n = int(input("Enter the value of N: "))
for i in range(n):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
