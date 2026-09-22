# MRO (Method Resolution Order) - solves the "diamond problem"
#
#         A
#        / \
#       B   C
#        \ /
#         D
#
# B and C both inherit from A. D inherits from both B and C.
# When D calls greet(), which version runs - A's, B's, or C's?
# Python decides this using MRO: search left to right through
# the parents as listed in the class definition (via C3 linearization).

class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):     # B listed first -> B is checked before C
    pass

# class D(C, B):    # swap order -> C checked before B -> output changes to "Hello from C"
#     pass

d = D()
print(d.greet())      # D has no greet() itself -> Python checks B next (per MRO) -> "Hello from B"
print(D.__mro__)       # shows the exact search order: D -> B -> C -> A -> object