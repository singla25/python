# Static Method:
# A static method belongs to a class but does not need access
# to either the object (self) or the class (cls).

# problem: Add a static method to the Car class that returns a general description of a Car

class Car:
    total_cars = 0
    total_fuel_cars = 0

    def __init__(self, brand, model, is_fuel_car=True):
        self.brand = brand
        self.model = model

        Car.total_cars += 1

        if is_fuel_car:
            Car.total_fuel_cars += 1

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
    total_electric_cars = 0

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model, is_fuel_car=False)

        self.battery_size = battery_size

        ElectricCar.total_electric_cars += 1

    def electric_car_details(self):
        return (
            f"Brand: {self.brand}, "
            f"Model: {self.model}, "
            f"Battery Size: {self.battery_size}"
        )

    def fuel_type(self):
        return "Electric"


# Creating objects
my_car = Car("Tata", "Safari")
my_car2 = Car("Toyota", "Corolla")

my_electric_car = ElectricCar("Tesla", "Model S", "85kWh")
my_electric_car2 = ElectricCar("BYD", "Seal", "82kWh")

# Class variable
print("Total Cars:", Car.total_cars)
print("Petrol/Diesel Cars:", Car.total_fuel_cars)
print("Electric Cars:", ElectricCar.total_electric_cars)

# Without @staticmethod:
# Object call -> Python automatically passes the object as self.
# print(my_car.general_description())

# Class call -> Python does not automatically pass an object,
# so the object must be passed explicitly.
# print(Car.general_description(my_car))


# With Static Method
print("General Description:", Car.general_description())
print("Is Valid Year:", Car.is_valid_year(2025))

print("General Description:", ElectricCar.general_description())

print(my_car.general_description())
print(my_car.is_valid_year(2020))