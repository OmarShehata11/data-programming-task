num = int(input("Enter a number: "))
if num < 0:
    print("The number is negative")

else:
    sum = 0

    for i in range(1, num+1):
        sum += i

    print("The sum from 1 to", num, "is", sum)
