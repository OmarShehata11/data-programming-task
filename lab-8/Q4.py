import math

def recpol(x, y):
  r = math.sqrt(x**2 + y**2)
  theta = math.atan2(y, x)
  return r, theta


x = int(input("enter x > "))
y = int(input("enter y > "))

r, theta = recpol(x, y)

print(f"Rectangular coordinates: ({x}, {y})") 
print(f"Polar coordinates: ({r:.3f}, {theta:.3f})")
