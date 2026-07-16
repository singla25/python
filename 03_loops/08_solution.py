# Prime Numbers

number = int(input("Enter your number: "))

is_prime = True

if number < 0: 
    print("Enter a Valid Number")
    exit()

for i in range(2, number):
    if (number % i) == 0:
        is_prime = False
        break

print(f"{number} is a prime number") if is_prime == True else print(f"{number} is not a prime number") 