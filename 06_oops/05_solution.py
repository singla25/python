# Polymorphism - One interface/method name, but different behavior depending on the object.

# Method overriding - Method overriding is one common way to achieve polymorphism.

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

class HydrogenCar(Car):
    def fuel_type(self):
        return "Hydrogen"


my_car = Car("Tata", "Safari")
print(my_car.car_details())
print("Fuel Type:", my_car.fuel_type())

my_electric_car = ElectricCar("Tesla", "Model S", "85kWh")
print(my_electric_car.electric_car_details())
print("Fuel Type:", my_electric_car.fuel_type())

my_hydrogen_car = HydrogenCar("Toyota", "Mirai")
print(my_hydrogen_car.car_details())
print("Fuel Type:", my_hydrogen_car.fuel_type())

cars = [my_car, my_electric_car, my_hydrogen_car]

for car in cars:
    print("Fuel Type:",car.fuel_type())


cars = [
    Car("BMW", "X5"),
    ElectricCar("MG", "Cyberster", "375kWh"),
    HydrogenCar("Hyundai", "Nexo")
]

for car in cars:
    print("Fuel:", car.fuel_type())




# Polymorphism without inheritance
class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

class Cow:
    def sound(self):
        return "Moo"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.sound())
