# Write a function that greets a user. if no name is provided, it should greet with a default name.

# def greet(name):
#     return "Hello, " + name + "!"

# name = input("Enter your name: ")

# n = "Guest" if name == "" else name
# username = greet(n)

# print(username)

def greet(name="Guest"):
    return "Hello, " + name + "!"

name = input("Enter your name: ")

username = greet(name or "Guest")
print(username)