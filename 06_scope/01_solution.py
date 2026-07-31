# Find maximum number

# def outer():
#     x = 10

#     def inner(x):
#         # nonlocal x
#         x = x+10
#         print(x)

#     inner()
#     print(x)

# outer()

x = "Global"

def outer():

    y = "Outer"

    def inner():

        z = "Local"

        print(z)
        print(y)
        print(x)
        print(len([1,2,3]))

    inner()

outer()