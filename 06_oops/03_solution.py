# Inheritance - Create an ElectricCar class that inherits from the Car class and an additional attribute battery size

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"Brand: {self.brand} and Model: {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        # self.brand = brand
        # self.model = model
        super().__init__(brand, model)  # Call the parent class constructor to initialize brand and model
        self.battery_size = battery_size

    def electric_car_details(self):
        return f"Brand: {self.brand}, Model: {self.model}, Battery Size: {self.battery_size}"

electric_car = ElectricCar("Tesla", "Model S", "100 kWh")
print(electric_car.electric_car_details())
print(electric_car.full_name())  # This will call the method from the parent class