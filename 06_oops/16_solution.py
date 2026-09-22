# Composition ("has-a" relationship)
#
# Instead of inheriting from another class, your class CONTAINS an
# instance of another class as an attribute. A Car HAS an Engine -
# it isn't an Engine. This is an alternative to inheritance for
# relationships that aren't really "is-a".
#
# Favor composition over inheritance: it's more flexible and avoids
# messy multi-parent hierarchies (like MRO conflicts) for relationships
# that are really "uses/has", not "is".

class Engine:
    def start(self):
        return "Engine started"

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

    def battery_info(self):
        return f"Battery Capacity: {self.capacity}"

class Car:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand
        self.model = model
        self.engine = Engine()                     # Car HAS an Engine (composition)
        self.battery = Battery(battery_capacity)    # Car HAS a Battery (composition)

    def start_car(self):
        return self.engine.start()          # delegation: Car doesn't start itself,
                                             # it asks its Engine object to do it

    def car_details(self):
        return f"{self.brand} {self.model}, {self.battery.battery_info()}"


my_car = Car("Tesla", "Model S", "85kWh")
print(my_car.start_car())        # Engine started
print(my_car.car_details())      # Tesla Model S, Battery Capacity: 85kWh