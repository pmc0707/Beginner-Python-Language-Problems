heads = int(input("Enter the number of heads: "))
feet = int(input("Enter the number of feet: "))
goats = (feet - 2 * heads) / 2
chickens = heads - goats
print("Number of chickens:", chickens)
print("Number of goats:", goats)
