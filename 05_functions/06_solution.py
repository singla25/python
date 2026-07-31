# Create a lambda function to compute the cube of a number

# we also do this also
# def cube(n):
#     return n**3

cube = lambda num: num**3

n = int(input("Enter the number: "))
result = cube(n)
print(result)