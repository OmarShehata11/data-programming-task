friends = input("Friends: ").split()
presents = input("Presents: ").split()

want = input("What is in his mind: ")

if want in presents:
  index = presents.index(want)
  name = friends[index]

  print(f"Oh {name}, Thank you friend :)")

else:
  print("Opps, Sorry none.")
