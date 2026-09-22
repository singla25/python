# Abstraction: hides HOW something works, forces WHAT must exist.
# The parent class defines a required method (a contract); it doesn't implement it.

# abstractmethods are methods that are declared in an abstract class but do not have any implementation/code. Subclasses of the abstract class must provide an implementation for these methods.

# @abstractmethod = declared, no implementation. Subclasses MUST override it.

# abc module = Python's built-in tool for defining abstract base classes (ABCs).
# It gives you ABC (to mark a class as abstract) and @abstractmethod (to mark
# required methods) so you can enforce an interface on subclasses.

# A class becomes "abstract" only if it inherits ABC AND has >=1 @abstractmethod.
# No abstract method -> it's just a normal class, can be instantiated directly.

# Abstract class = blueprint, can't be instantiated (TypeError if you try).
# Concrete class = implements ALL abstract methods -> can be instantiated.


from abc import ABC, abstractmethod

class BankApp(ABC):

    def database(self):          # concrete method, shared as-is by all subclasses
        return "Connected to database."

    @abstractmethod
    def security(self):          # no body -> every subclass MUST define this
        pass


class MobileApp(BankApp):        # implements security() -> becomes concrete, can be instantiated

    def mobile_login(self):
        return "Logged in through mobile app."

    def security(self):
        return "Mobile app security enabled."

mobile_app = MobileApp()
print(mobile_app.database())






from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def fuel_type(self):
        pass   # no implementation here — subclasses must provide one

    def vehicle_details(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric Charge"

my_car = Car("Toyota", "Corolla")
print(my_car.fuel_type())

