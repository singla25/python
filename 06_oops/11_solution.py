# @classmethod - @classmethod gets cls (the class itself) automatically, instead of self (the instance). That means it can access/modify class variables, and it's commonly used to create alternate constructors — extra ways to build an object besides the normal __init__.


class Car:

    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    @classmethod
    def from_string(cls, car_string):
        brand, model = car_string.split(",")
        return cls(brand, model)   # same as Car(brand, model)

    @classmethod
    def car_count(cls):
        return cls.total_cars

my_car = Car.from_string("Toyota,Corolla")
print(my_car.brand, my_car.model)

my_car2 = Car("Tata", "Safari")
my_car3 = Car.from_string("Honda,City")
print(Car.car_count())

