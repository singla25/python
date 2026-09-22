# Pratice

class Person:
    def __init__(self, age):
        if age > 0:
            self.age = age
        else:
            raise ValueError("Age cannot be negative or 0")

person = Person(25)

print(person.age)   # Get
person.age = -100   # Set
print(person.age)   # -100 because python says Okay, store -100 in the age attribute.



class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            raise ValueError("Age cannot be negative or 0")

    def person_info(self):
        return f"Name: {self.name}, Age: {self.age}"
    

class Employee(Person):

    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            raise ValueError("Salary cannot be negative or 0")

    @staticmethod
    def company_policy():
        return "Employees must follow company policies."

    def employee_info(self):
        return f"Employee ID: {self.employee_id}, Salary: {self.salary}"

class Developer(Employee):

    def __init__(self, name, age, employee_id, salary, programming_language, experience):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language
        self.experience = experience

    def developer_info(self):
        return (
            f"Programming Language: {self.programming_language}, "
            f"Experience: {self.experience} years"
        )

    def write_code(self):
        return f"{self.name} is writing code in {self.programming_language}."


developer = Developer("Sahil", 25, "EMP101", 60000, "Python", 1)

print(developer.person_info())
print(developer.employee_info())
print(developer.developer_info())
print(developer.write_code())


print(isinstance(developer, Developer))
print(isinstance(developer, Employee))
print(isinstance(developer, Person))

print(developer.company_policy())