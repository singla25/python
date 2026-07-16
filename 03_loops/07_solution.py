# Run loop until user put number in between 1 to 10 only

while True:
    number = int(input("Enter balue b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")
