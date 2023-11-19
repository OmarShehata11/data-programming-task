def CountItems(l):
    if l == []:
        return 0 
    count = 1
    count = count + CountItems(l[1:])
    return count

l = input("enter the list elemnts: ").split()
l = [int(x) for x in l]
print(CountItems(l))
