fruits = int(input("how many fruit do you like "))
mgaFruits = []

for i in range(fruits):
    ask = input("WHAT YOUR FAVORITE FRUIT : ")
    mgaFruits.append(ask)

    print(mgaFruits)
    
    for fruits in mgaFruits:
        if fruits == "banana":
            print()
            break
        elif fruits == "apple":
            print(f"HAPPY EATING")