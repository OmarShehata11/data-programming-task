def GetPositiveArray(string):
    arr = input(string).split()
    i = 0
    while i != len(arr) :
        if int(arr[i]) < 0 :
            i = 0
            arr = input("Error! " + string).split()
            continue
        arr[i] = int(arr[i])
        i = i +1
    return arr

def ComputeAverage(wait):
    return sum(wait)/len(wait)

def GetIDLongWait(id, wait, avg):
    waitList = []
    for i in range(len(id)):
        if wait[i] > avg:
            waitList.append(id[i])
    return waitList


id = GetPositiveArray("Enter ID list: ")

wait = GetPositiveArray("Enter Waiting Time List: ")

avg = ComputeAverage(wait)
print("average waiting time = %.2f\n" %avg)

idlongwait= GetIDLongWait(id, wait, avg)

print("IDs for customers who waited longer than average are: ")
print(idlongwait)
