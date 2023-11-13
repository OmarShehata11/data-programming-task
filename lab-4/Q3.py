soup_menu = ["vegetables", "seafood", "mushroom"]
meal_menu = ["burger", "grilled chicken", "mashed potatoes"]

vegetables = ["vegetables", "mushroom", "mashed potatoes"]

print(f"soup menu: {soup_menu}\nmeal menu: {meal_menu}\n")

soup = input("soup: ")
meal = input("meal: ")

if soup in vegetables and meal in vegetables:
    print("she loves vegetables\n")
elif soup in vegetables or meal in vegetables:
    print("she neither hates or loves vegetables\n")
else:
    print("she hates vegetables\n")



