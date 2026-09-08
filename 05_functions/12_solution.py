# 1. Local, Enclosing, Global and Built-in Function

# x = "Global"
# def outer():
#     y = "Enclosing"
#     def inner():
#         global x
#         x = "Changed Global Variable"

#         nonlocal y
#         y = "Changed Outer Variable"

#         z = "Local"
        
#         print("Z", z)
#         print(y)
#         print(x)
#         print(len([1,2,3]))
#     inner()
#     print("Y:", y)    
# outer()
# print("X:", x)


# x = 99

# def func(y):
#     z = x+y
#     return z

# result = func(1)
# print(result)


# 2. Global
# x = 99

# def func1():
#     global x
#     x = 88

# func1()
# print(x)


# 3. Local
# x = 99

# def func(y):
#     x = 80
#     print(x) #80
#     z = x+y
#     return z

# result = func(1)
# print(result) #81


# 4. Enclosing
# x = 99

# def f1():
#     x = 88

#     def f2():
#         print(x)
#     f2()

# f1()
# print(x)


# 5. nonlocal
# x = 99

# def f1():
#     x = 88

#     def f2():
#         nonlocal x
#         x = 50
#         print("F2:", x)
#     f2()
#     print("F1:", x)

# f1()
# print("Global:", x)
 


# x = 99

# def f1():
#     x = 88

#     def f2():
#         print("F2:", x)
#     return f2 


# myResult = f1()
# myResult()



# def chaicoder(num):
#     def actual(x):
#         return x ** num
#     return actual

# f = chaicoder(2)(3)
# print(f)




def countdown(n):
  if n < 0:
    return "Invalid Input"
  
  if n == 0:
    print("Blastoff!")
  
  else:
    print(n)
    countdown(n - 1)

print(countdown(5))


def counter():

    count = 0

    def increment():

        nonlocal count

        count += 1

        return count

    return increment

click = counter()
print(click())
print(click()) 