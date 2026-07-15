password = input("Enter Your Password: ")
length = len(password)

if length < 6:
    strength = "Weak"
elif length <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print(f"Strength of your {password} is", strength)