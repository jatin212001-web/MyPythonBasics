hungry = input("Are you hungry? (yes/no): " ).strip().lower()
if hungry == "yes":
    print("Let's get some food!")   
    print("Here are some options:")
    print("1. Pizza")
    print("2. Salad")
    print("3. Sandwich")
elif hungry == "no":
    print("Great! Let's continue working.")
