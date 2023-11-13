length = input("enter the lenght of rectangles: ").split()
width = input("enter the width of rectangles in the same order: ").split()

length = [float(y) for y in length]
width = [float(x) for x in width]

print("Num\t\tLength\t\tWidth\t\tArea(approx.)\n")

for i in range(len(length)):
    print("%3.0d\t\t%4.2f\t\t%3.2f\t\t%.0f\n" %(i+1, length[i], width[i], length[i]*width[i]))
