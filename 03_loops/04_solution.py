# Reverse a String

string = input("Enter your string: ")
reverse_string = ""

for s in string:
    reverse_string = s + reverse_string

print(reverse_string)