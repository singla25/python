# Class Method and Self - Add a method to the Car class that displays the full name of the car (Brand and Model)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"Brand: {self.brand} and Model: {self.model}"

my_car = Car("Toyota", "Corolla")
my_new_car = Car("Tata", "Safari")

print(my_car.full_name())
print(my_new_car.full_name())

        