def Check(soap, meal):
    vegetables = ["vegetables", "mushroom", "mashed potatoes"]
    
    for i in vegetables:
        if i in soap or i in meal:
            print("she loves vegetables\n")
            return 
    
    print("she hates vegetables\n")
    


soap = input("soap: ").split()
meal = input("meal: ").split()


Check(soap, meal)
