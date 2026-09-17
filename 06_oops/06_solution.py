# Add a class variable to Car that keeps track of the number of car created and also check how many different type of cars created on the basis of fuel type

class Car:
    total_car = 0
    total_fuel_car = 0

    def __init__(self, brand, model, is_fuel_car=True):
        self.brand = brand
        self.model = model

        Car.total_car += 1

        if is_fuel_car:
            Car.total_fuel_car += 1

    def car_details(self):
        return f"Brand: {self.brand} and Model: {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    total_electric_car = 0

    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model, is_fuel_car=False)
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

print("Total Cars:", Car.total_car)
print("Petrol/Diesel Cars:", Car.total_fuel_car)
print("Electric Cars:", ElectricCar.total_electric_car)