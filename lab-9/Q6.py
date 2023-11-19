def GetListSum(l):
    if l == []:
        return 0
    sum = l[0]
    sum = sum + GetListSum(l[1:])
    return sum


l = input("enter the list values: ").split()
l = [ int(x) for x in l ]
print(GetListSum(l))
