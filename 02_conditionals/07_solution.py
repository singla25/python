order_size = input("Enter your Coffee Cup Size (Small, Medium, Large): ").upper()
extra_shot = input("How many extra espresso shots? (Press Enter for 0): ")

if extra_shot == "":
    extra_shot = 0
else:
    extra_shot = int(extra_shot)

if extra_shot > 0:
    coffee = f"{order_size} Coffee with {extra_shot} extra espresso shot(s)"
else:
    coffee = f"{order_size} Coffee"

print(coffee)