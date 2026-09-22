# Encapsulation - Encapsulation means making variables private.

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




class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(10000)
account.deposit(5000)
account.withdraw(2000)
account.withdraw(20000) # this dorsn't executes here, our condition doesn't satisfies 
print("Amount:", account.get_balance())






# Getter (get/read data) and Setter(changes/updates data)
# Method 1
class Person1:
    def __init__(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age

person1 = Person1(25)
print(person1.get_age())
person1.set_age(30)
print(person1.get_age())




#  Method 2
class Person2:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Age cannot be negative or 0")

person2 = Person2(20)
print(person2.age)
person2.age = 25
print(person2.age)