# Static Method - A static method is a method that belongs to a class but doesn't need access to either the object (self) or the class (cls)

# problem: Add a static method to the Car class that returns a general description of a Car


class Car:
    total_car = 0
    total_fuel_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        # self.total_car += 1 # not good approach this creates the instance for each object not for particular class (Car)
        Car.total_car += 1 
        Car.total_fuel_car += 1

    def car_details(self):
        return f"Brand: {self.brand} and Model: {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are the mean of transport"

    @staticmethod
    def is_valid_year(year):
        return year >= 1886

class ElectricCar(Car):
    total_electric_car = 0

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

        ElectricCar.total_electric_car += 1

    def electric_car_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Battery Size: {self.battery_size}"

    def fuel_type(self):
        return "Electric Charge"


my_car = Car("Tata", "Safari")
my_car2 = Car("Toyota", "Corolla")

my_electric_car = ElectricCar("Tesla", "Model S", "85kWh")
my_electric_car2 = ElectricCar("BYD", "Seal", "82kWh")

# print("Total Cars:", Car.total_car)
# print("Petrol/Diesel Cars:", Car.total_fuel_car)
# print("Electric Cars:", ElectricCar.total_electric_car)

# Without @staticmethod
# print(my_car.general_description()) # here we need self because we want to access method through object
# print(Car.general_description()) # here we don't need self because we want to access method directly through class

# With Static Method
print(my_car.general_description())
print(Car.general_description())

print(Car.is_valid_year(2025))
print(my_car.is_valid_year(2020))