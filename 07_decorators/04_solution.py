# Closure
# A closure is a function that remembers variables
# from its enclosing function even after it finishes.

def chaicoder(num):

    # Inner function uses 'num' from the outer function.
    def actual(x):
        return x ** num

    # Return the function itself.
    return actual


# chaicoder(2) returns actual function with num = 2.
# Then (5) calls that returned function with x = 5.
f = chaicoder(2)(5)

print(f)  # 25


# Same thing written step-by-step:
power = chaicoder(2)  # power remembers num = 2
result = power(5)     # 5 ** 2

print(result)         # 25