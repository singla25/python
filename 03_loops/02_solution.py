number = int(input("Enter the value of n: "))

no_of_even = 0
sum = 0

for num in range(1, number+1):
    if num % 2 == 0:
        no_of_even += 1
        sum += num

print(f"Number of even number in 1 to {number} is {no_of_even} and their sum is {sum}")