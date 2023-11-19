def FMConversion(f):
    if f < 0:
        print("error, negative value\n")
        return 
    print("================================\n")
    print("feet\t\tmeter\n")
    for i in range(1, f+1):
        print("%4d\t\t%5f\n" %(i, i*0.3048))

    print("================================\n")




n = int(input("enter N: "))
FMConversion(n)
