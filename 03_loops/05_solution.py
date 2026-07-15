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
