def getSum(n):
    sum = 0
    if n != 0:
        sum = n**2
        sum = sum + getSum(n-1)
    return sum

n = int(input("enter the n > "))

print(getSum(n))
