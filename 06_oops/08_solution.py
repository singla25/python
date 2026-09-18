# Property Decorators
# Property Decorator (@property) allows you to access a method like an attribute while controlling how its value is read or modified.


# Problem : Use a property decorator in the class to make the model attribute read-only. 

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model

    def car_details(self):
        return f"Brand: {self.brand} and Model: {self.__model}"

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
        super().__init__(brand, model)
        self.battery_size = battery_size

    def electric_car_details(self):
        return (
            f"Brand: {self.brand}, "
            f"Model: {self.__model}, "
            f"Battery Size: {self.battery_size}"
        )

    def fuel_type(self):
        return "Electric"


# Creating objects
my_car = Car("Tata", "Safari")
my_car2 = Car("Toyota", "Corolla")
my_electric_car = ElectricCar("Tesla", "Model S", "85kWh")
my_electric_car2 = ElectricCar("BYD", "Seal", "82kWh")

print(my_car.model)
# my_car.model = "Nano"
print(my_electric_car.model)



# Getter and Setter Method
class Person:
    def __init__(self, age):
        self.__age = age

    # Getter
    @property
    def age(self):
        return self.__age

    # Setter
    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative or 0")



person = Person(25)

# Getter
print(person.age)

# Setter
person.age = 30
print(person.age)

# Invalid value
person.age = -10
print(person.age)