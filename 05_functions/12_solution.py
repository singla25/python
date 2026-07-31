# Find maximum number

def outer():
    x = 10

    def inner(x):
        # nonlocal x
        x = x+10
        print(x)

    inner()
    print(x)

outer()