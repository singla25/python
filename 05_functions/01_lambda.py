# lambda arguments : expression

# def myfunc(n):
#   return lambda a : a * n

# mytripler = myfunc(3)
# print(mytripler(11))


# 1. Lambda with map() function
# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)



# 2. Lambda with filter() function
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print(odd_numbers)



# 3. Lambda with sorted() function
# students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)



# words = ["apple", "pie", "banana", "cherry"]
# sorted_words = sorted(words, key=lambda x: len(x))
# print(sorted_words)




student = {
    "name": "Sahil",
    "age": 24,
    "city": "Mohali"
}

student.values()

print(student.values())
