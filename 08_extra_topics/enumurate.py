# enumerate()
# enumerate() adds an index number to each item of an iterable.

x = ('Masala', 'lemon', 'ginger')

# enumerate() returns an enumerate object (iterator).
y = enumerate(x)

# Convert the enumerate object into a list.
# Result:
# [(0, 'Masala'), (1, 'lemon'), (2, 'ginger')]
print(list(y))


# We can also use enumerate() directly in a for loop.
for index, value in enumerate(x):
    print(index, value)


# By default, the index starts from 0.
# We can change the starting index using start=.
for index, value in enumerate(x, start=1):
    print(index, value)