# Factoial Calculation

num = int(input("Enter your number: "))

original_num = num
fact = 1

while num > 0:
    fact = fact * num
    num = num - 1

print(f"{original_num}! = {fact}")