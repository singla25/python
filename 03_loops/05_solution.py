# Find count of character and first non repeating character

string = input("Enter your string: ")

count_of_character = {}

for ch in string:
    if ch in count_of_character:
        count_of_character[ch] += 1
    else:
        count_of_character[ch] = 1

print(count_of_character)

for ch in string:
    if count_of_character[ch] == 1:
        print(f"First non-repeating character is '{ch}'")
        break

# for ch in string:
#     if string.count(ch) == 1:
#         print(f"First non-repeating character is '{ch}'")
#         break


non_repeating = []

for ch in string:
    if count_of_character[ch] == 1:
        non_repeating.append(ch)

print(non_repeating)


count = {}

for char in string:
    count[char] = count.get(char, 0) + 1

print(count)

# If char already exists → get its current count
# If it doesn't exist → use 0
# Then + 1
