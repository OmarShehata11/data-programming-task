import math

def get_input():
  degree = float(input("Enter angle in degrees: "))
  return degree


def convert(degree):
  radian = degree * (math.pi/180) 
  return radian

def show(value):
  print(f"Angle in radians: {value}")

degree = get_input()
radian = convert(degree)
show(radian)
