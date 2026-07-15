fruit = input("Enter your Fruit Name: ").upper()
color = input("Enter your Fruit Color: ").upper()

if fruit == "BANANA":
    if color == "GREEN":
        print(f"Your {fruit} is Unripe")
    elif color == "YELLOW":
        print(f"Your {fruit} is Ripe")
    elif color == "BROWN":
        print(f"Your {fruit} is Overripe")