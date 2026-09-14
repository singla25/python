# Encapsulation - It is a fundamental concept in object-oriented programming (OOP) that restricts direct access to an object's attributes and methods. It allows for controlled access through public methods, ensuring that the internal state of an object is protected from unintended interference and misuse.

# Problem: Modify the Car Class to encapsulate the brand attribute, making it private and provide a getter method to access it.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand # Making the brand attribute private
        self.model = model

    def get_brand(self):
        return self.__brand + " is the brand of the car."

    def full_name(self):
            return f"Brand: {self.__brand} and Model: {self.model}"

my_car = Car("Toyota", "Corolla")
# print(my_car.__brand) # This will raise an AttributeError
print(my_car.get_brand())
print(my_car.full_name())