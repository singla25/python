# Operator Overloading
# Lets you define what built-in operators (+, -, <, ==, len(), etc.)
# do when used on your own custom objects.
# Without this, using +/< on a custom object raises a TypeError.

# __add__(self, other)  -> defines behavior of `self + other`
# __lt__(self, other)   -> defines behavior of `self < other`
# __str__(self)         -> defines what print(obj) / str(obj) shows

# Convention: __add__ should return a NEW object, not mutate self.
# This matches how built-in types behave (e.g. a + b doesn't change a).

class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Wallet(self.amount + other.amount)   # combine two wallets into a new one

    def __lt__(self, other):
        return self.amount < other.amount           # compares based on amount

    def __str__(self):
        return f"Wallet(₹{self.amount})"


w1 = Wallet(500)
w2 = Wallet(300)

combined = w1 + w2          # Python calls w1.__add__(w2) behind the scenes
print(combined)             # uses __str__ -> Wallet(₹800)

print(w1 < w2)               # Python calls w1.__lt__(w2) -> False (500 is not < 300)