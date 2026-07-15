numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

negative_number_count = 0
positive_number_count = 0

for num in numbers:
    if num > 0:
        positive_number_count += 1
    if num < 0:
        negative_number_count += 1

print(positive_number_count)
print(negative_number_count)