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
# def even_generator(n):
#     for i in range(2, n + 1, 2):
#         yield i

# n = int(input("Enter number: "))

# for num in even_generator(n):
#     print(num)




# Counter
# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# n = int(input("Enter number: "))

# for num in count_up_to(n):
#   print(num)


def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

