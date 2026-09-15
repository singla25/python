# Polymorphism - One interface/method name, but different behavior depending on the object.

# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def car_details(self):
        return f"Brand: {self.brand} and Model: {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def electric_car_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Battery Size: {self.battery_size}"

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Tata", "Safari")
print(my_car.car_details())
print(my_car.fuel_type())

my_electric_car = ElectricCar("Tesla", "Model S", "85kWh")
print(my_electric_car.electric_car_details())
print(my_electric_car.fuel_type())
