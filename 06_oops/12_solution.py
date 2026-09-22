# Dunder (magic) methods

# __str__(self) — controls what print(obj) or str(obj) shows. Meant to be human-readable.
# __repr__(self) — controls what shows in the console/debugger, or when str isn't defined. Meant to be unambiguous, ideally something you could copy-paste to recreate the object.


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}')"

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model

my_car = Car("Toyota", "Corolla")
print(my_car)        # uses __str__  -> Toyota Corolla
print([my_car])       # uses __repr__ -> [Car('Toyota', 'Corolla')]

car1 = Car("Toyota", "Corolla")
car2 = Car("Toyota", "Corolla")
print(car1 == car2)   # False, without __eq__ defined, even though brand/model match!

car3 = Car("Honda", "City")
print(car1 == car3)   # should be False