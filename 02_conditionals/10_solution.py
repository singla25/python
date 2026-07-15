species = input("Enter the species of your pet: ").strip().upper()
age = int(input("Enter the age of your pet: "))

if age < 0:
    print("Age cannot be negative.")

elif species == "DOG":
    if age < 2:
        print("Puppy Food")
    elif age < 6:
        print("Dog Food")
    else:
        print("Senior Dog Food")

elif species == "CAT":
    if age < 2:
        print("Baby Cat Food")
    elif age < 5:
        print("Cat Food")
    else:
        print("Senior Cat Food")

else:
    print("Invalid species")