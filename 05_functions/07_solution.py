# Write a function that takes variable number of arguments and return their sum

# Method 1
# def sum_all(listofnum):
#     sum = 0
#     for num in listofnum:
#         sum += int(num)
#     return sum

# n = input("Enter numbers separated by spaces: ")
# listofnum = n.split()

# result = sum_all(listofnum)
# print(result)



# Method 2
def sum_all(*args):
    print(args)
    for i in args:
        print(i)
    return sum(args)

n = input("Enter numbers separated by spaces: ")

numbers = [int(num) for num in n.split()]

result = sum_all(*numbers)

print(result)
