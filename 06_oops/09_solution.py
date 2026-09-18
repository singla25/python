# Class Inheritance and isinstance() Function
# Inheritance allows a child class to reuse the attributes and methods of a parent class.
# isinstance() checks whether an object belongs to a particular class or any of its parent classes.


# isinstance(object, class) checks whether an object is an instance of the given class or one of its subclasses.


# Child object is also considered an instance of its parent, but parent object is not an instance of its child.

# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_details(self):
        return f"Brand: {self.brand} and Model: {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are a means of transportation."

    @staticmethod
    def is_valid_year(year):
        return year >= 1886


class ElectricCar(Car):

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def electric_car_details(self):
        return (
            f"Brand: {self.brand}, "
            f"Model: {self.model}, "
            f"Battery Size: {self.battery_size}"
        )

    def fuel_type(self):
        return "Electric"


# Creating objects
my_safari = Car("Tata", "Safari")
my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print("my_tesla isinstance of Electric Car:", isinstance(my_tesla, ElectricCar))
print("my_tesla isinstance of Car:", isinstance(my_tesla, Car))

print("my_safari isinstance of Electric Car:", isinstance(my_safari, ElectricCar))
print("my_safari isinstance of Car:", isinstance(my_safari, Car))
