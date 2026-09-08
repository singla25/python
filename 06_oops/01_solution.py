# Basic Class and Object - Create class with attributes like brand and model. Then create an instance of this class

# Method 1
# class Car:
#     brand = None 
#     model = None

# my_car = Car()
# my_car.brand = "Toyota"
# my_car.model = "Camry"

# print(my_car.brand)
# print(my_car.model)
# print(my_car)


# Method 2
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)

my_new_car = Car("Tata", "Safari")
print(my_new_car.model)


