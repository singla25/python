# Multiple Inheritance
# Multiple inheritance means a single child class inherits from multiple parent classes.


# Multiple inheritance allows a class to inherit attributes and methods from more than one parent class.


# Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_details(self):
        return f"Brand: {self.brand} and Model: {self.model}"

class Battery:

    def __init__(self, battery_size):
        self.battery_size = battery_size

    def battery_info(self):
        return f"Battery Size: {self.battery_size}" 

class Engine:

    def start_engine(self):
        return "Engine started"


class ElectricCar(Car, Battery, Engine):

    def __init__(self, brand, model, battery_size):
        Car.__init__(self, brand, model)
        Battery.__init__(self, battery_size)

    def electric_car_details(self):
        return (
            f"Brand: {self.brand}, "
            f"Model: {self.model}, "
            f"Battery Size: {self.battery_size}"
        )


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")

print(my_tesla.car_details())
print(my_tesla.battery_info())
print(my_tesla.start_engine())
print(my_tesla.electric_car_details())