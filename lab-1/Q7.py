X =int(input("enter x : "))
Y = int(input("enter y: "))
N = X // Y
if X % Y != 0:
	N += 1
print(N)
