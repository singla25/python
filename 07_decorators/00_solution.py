# ============================================================
# DECORATORS
# ============================================================
#
# A decorator is a function that modifies or extends the
# behaviour of another function without changing the original
# function's code.
#
# Basic flow:
#
#     Original Function
#            ↓
#        Decorator
#            ↓
#     Wrapper Function
#            ↓
#     Modified Behaviour
#
# The @decorator syntax is basically a shorter way of writing:
#
#     function = decorator(function)
# ============================================================


def my_decorator(func):
    """
    A simple decorator that adds behaviour before and after
    the original function runs.
    """

    def wrapper():
        # Code that runs BEFORE the original function
        print("Before function")

        # Call the original function
        func()

        # Code that runs AFTER the original function
        print("After function")

    # Return the wrapper function.
    #
    # The wrapper will replace the original function.
    return wrapper


# Using the decorator with @ syntax
#
# This:
#
#     @my_decorator
#     def say_hello():
#
# is approximately equivalent to:
#
#     say_hello = my_decorator(say_hello)
#
@my_decorator
def say_hello():
    print("Hello Sahil")

# Because say_hello has been decorated, calling it actually
# executes the wrapper function.
say_hello()


# ============================================================
# REAL-LIFE EXAMPLE: LOGIN REQUIRED
# ============================================================
#
# Imagine we have functions that should only be accessible
# when the user is logged in.
#
# Instead of writing the login-checking code inside every
# function, we can create a decorator and reuse it.
# ============================================================

# For this example, we use a simple variable to represent
# whether the user is logged in or not.

logged_in = False

def login_required(func):
    """
    Decorator that allows a function to run only when the
    user is logged in.
    """

    # *args and **kwargs allow the decorator to work with
    # functions that accept positional and keyword arguments.
    def wrapper(*args, **kwargs):

        # Check whether the user is logged in.
        if not logged_in:
            print("Please login first")
            return

        # If the user is logged in, execute the original
        # function with all of its arguments.
        return func(*args, **kwargs)

    return wrapper


@login_required
def dashboard():
    print("Welcome to dashboard")


# logged_in = False
#
# The decorator stops dashboard() from running.
dashboard()


# ============================================================
# DECORATOR WITH FUNCTION ARGUMENTS
# ============================================================
#
# A decorator should ideally be able to work with functions
# that have different numbers/types of arguments.
#
# That's why we use:
#
#     *args
#     **kwargs
#
# *args  -> collects positional arguments
# **kwargs -> collects keyword arguments
# ============================================================


@login_required
def profile(username):
    print(f"Welcome to your profile, {username}")


# Currently logged_in is False, so the function will not run.
profile("Sahil")


# Now change the login state.
logged_in = True

print("\nUser logged in:\n")

# dashboard() can now execute.
dashboard()

# profile() can also execute and receive its argument.
profile("Sahil")


# ============================================================
# IMPORTANT DECORATOR CONCEPT
# ============================================================
#
# Consider:
#
#     @my_decorator
#     def say_hello():
#         print("Hello")
#
# Python treats it approximately as:
#
#     say_hello = my_decorator(say_hello)
#
# Therefore:
#
#     say_hello()
#
# actually calls the wrapper returned by my_decorator.
#
#
# The complete flow is:
#
#     say_hello()
#          ↓
#       wrapper()
#          ↓
#     "Before function"
#          ↓
#     original say_hello()
#          ↓
#     "Hello Sahil"
#          ↓
#     "After function"
#
# ============================================================