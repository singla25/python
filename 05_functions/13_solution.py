# Fibonacci Sequence - To calculate the current Fibonacci number, first calculate the previous two Fibonacci numbers.

def fibonacci(n):
  if n < 0:
    return "Invalid Input"
  
  if n <= 1:
    return n
  
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))


