# Write a generator function that yields even numbers upto a specified limit

# Method 1
# def even_generator(n):
#     for i in range(n+1):
#         if i % 2 == 0:
#            yield i 

# n = int(input("Enter number: "))

# for num in even_generator(n):
#     print(num)



# Method 2
def even_generator(n):
    for i in range(2, n + 1, 2):
        yield i

n = int(input("Enter number: "))

for num in even_generator(n):
    print(num)