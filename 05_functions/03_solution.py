# Write a function that multiplies two numbers, but can also accept and multiply strings

def multiply(a, b):
    return a * b

a = input("Enter first value: ")
b = input("Enter second value: ")

# Convert to int if possible
if a.isdigit():
    a = int(a)
else:
    print("Invalid input")

if b.isdigit():
    b = int(b)
else:
    print("Invalid input")

result = multiply(a, b)
print(result)