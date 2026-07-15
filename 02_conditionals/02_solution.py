age = int(input("Provide me your Age: "))
day = input("Today's Day: ").upper()

price = 12 if age > 18 else 8

if day == "WEDNESDAY":
    price = price - 2

print(f"Ticket price for you is ${price}")