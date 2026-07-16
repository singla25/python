# Check if all elements in alist are unique. If a duplicate is found, exit the loop and print the duplicate

fruits = ["apple", "mango", "orange", "apple", "mango"]

# new_list = []

# for fruit in fruits:
#     if fruit not in new_list:
#         new_list.append(fruit)
#     else:
#         print(f"Duplicate Fruit: {fruit}")
#         exit()

unique_item = set()

for item in fruits:
    if item in unique_item:
        print(f"Duplicate Fruit: {item}")
        break
    unique_item.add(item)