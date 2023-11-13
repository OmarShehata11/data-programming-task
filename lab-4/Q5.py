for i in range(5):
  weight = float(input("Enter weight: "))
  if weight < 0:
    print("Invalid weight")
    continue

  unit = int(input("Enter weight unit (1 for mg, 2 for kg, 3 for ton): "))
  
  if unit == 1: # mg
    print(weight)
    print("Converting mg to gram")
    weight_gram = weight / 1000

  elif unit == 2: # kg
    print(weight)      
    print("Converting kg to gram")
    weight_gram = weight * 1000

  elif unit == 3: # ton
    print(weight)
    print("Converting ton to gram")        
    weight_gram = weight * 1000000

  else:
    print("Invalid unit")
    continue

  print(weight_gram)

  choice = input("do you want to continue\n[y] yes\t[n] no\n")

  if choice == 'n':
      break
