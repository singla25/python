# Write a function that accept any number of keyboard arguments and prints them in the format

#  Method 1
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

data = {}

while True:
    key = input("Enter key (or 'done' to finish): ")

    if key.lower() == "done":
        break

    value = input(f"Enter value for '{key}': ")

    data[key] = value

print_kwargs(**data)



# Method 2
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_input = input("Enter key:value pairs separated by commas: ")

data = {}

pairs = user_input.split(",")

for pair in pairs:
    key, value = pair.split(":")
    data[key.strip()] = value.strip()

print_kwargs(**data)