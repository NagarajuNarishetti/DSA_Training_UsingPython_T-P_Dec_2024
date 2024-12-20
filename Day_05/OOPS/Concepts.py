# 1. State in Python
# - State refers to the current values of an object's attributes or properties.
# - In Python, the state of an object can be classified into two types: 
#   1. Instance (Non-static) state: Attributes specific to an instance of the class.
#   2. Class (Static) state: Attributes shared by all instances of a class.

class Dog:
    species = "Canis lupus familiaris"  # Class/Static State (Shared by all instances)

    def __init__(self, name, breed):
        self.name = name  # Instance State (Specific to each object)
        self.breed = breed  # Instance State (Specific to each object)

    def display_info(self):
        print(f"{self.name} is a {self.breed}.")

# Creating instances of Dog
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

dog1.display_info()  # Output: Buddy is a Golden Retriever.
dog2.display_info()  # Output: Max is a Bulldog.

# Accessing Class State
print(Dog.species)  # Output: Canis lupus familiaris


# 2. Properties in Python
# - Properties in Python are special methods that allow you to define custom getter, setter, and deleter methods for an attribute.
# - With properties, you can make your attributes behave like read-only or writable attributes, or apply validation rules when setting values.

class Circle:
    def __init__(self, radius):
        self._radius = radius  # Private variable for radius

    @property
    def radius(self):
        return self._radius  # Getter for radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")  # Setter with validation
        self._radius = value

    @property
    def area(self):
        return 3.14 * self._radius ** 2  # Computed property for area

# Creating an instance of Circle
circle = Circle(5)
print(circle.area)  # Output: 78.5 (Area calculated)

circle.radius = 10  # Setting a new radius
print(circle.area)  # Output: 314.0 (Area updated)

# Uncommenting the following line would raise a ValueError:
# circle.radius = -5  # ValueError: Radius cannot be negative


# 3. Generic Types in Python
# - Generic types in Python are a way to define classes or functions that can work with different data types.
# - The typing module provides support for specifying types that work with any data type.
# - `TypeVar` is used to define a generic type variable that can represent any type.

from typing import TypeVar, Generic

T = TypeVar('T')  # Define a generic type variable

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value  # The value can be of any type (generic)

    def get_value(self) -> T:
        return self.value  # Returns the value of the type

# Creating instances of Box with different types
box_int = Box(42)  # Box of integer
print(box_int.get_value())  # Output: 42

box_str = Box("Hello")  # Box of string
print(box_str.get_value())  # Output: Hello

box_float = Box(3.14)  # Box of float
print(box_float.get_value())  # Output: 3.14


# 4. Static vs Non-static State
# - Static state (class variables): Shared across all instances of a class.
# - Non-static state (instance variables): Unique to each instance of the class.

class Car:
    wheels = 4  # Static state (shared by all instances)

    def __init__(self, make, model):
        self.make = make  # Non-static state (unique to each instance)
        self.model = model  # Non-static state (unique to each instance)

    def display_info(self):
        print(f"{self.make} {self.model} has {Car.wheels} wheels.")

# Creating instances of Car class
car1 = Car("Tesla", "Model S")
car2 = Car("BMW", "X5")

car1.display_info()  # Output: Tesla Model S has 4 wheels.
car2.display_info()  # Output: BMW X5 has 4 wheels.

# Accessing static state directly
print(Car.wheels)  # Output: 4


# 5. Specific vs Generic State
# - **Specific state** refers to instance-specific attributes that are unique to each object.
# - **Generic state** refers to class-specific attributes that are shared by all objects of the class.

class Animal:
    species = "Unknown"  # Generic state (shared by all instances)

    def __init__(self, name, age):
        self.name = name  # Specific state (unique to each instance)
        self.age = age  # Specific state (unique to each instance)

    def display_info(self):
        print(f"{self.name} is {self.age} years old and belongs to species {Animal.species}.")

# Creating instances of Animal class
animal1 = Animal("Lion", 5)
animal2 = Animal("Elephant", 10)

animal1.display_info()  # Output: Lion is 5 years old and belongs to species Unknown.
animal2.display_info()  # Output: Elephant is 10 years old and belongs to species Unknown.

# Modifying the generic state (class-level attribute)
Animal.species = "Mammal"

animal1.display_info()  # Output: Lion is 5 years old and belongs to species Mammal.
animal2.display_info()  # Output: Elephant is 10 years old and belongs to species Mammal.


# 6. Static Methods vs Instance Methods
# - Static methods are methods that do not depend on instance variables and are called on the class itself.
# - Instance methods depend on instance variables and are called on an object instance.

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

# Using static methods directly on the class without creating an instance
print(Calculator.add(5, 3))  # Output: 8
print(Calculator.subtract(5, 3))  # Output: 2
print(Calculator.multiply(5, 3))  # Output: 15
print(Calculator.divide(5, 2))  # Output: 2.5


# Summary of Concepts:
# 1. **State**:
#    - Instance State: Attributes unique to each object (non-static).
#    - Class State: Attributes shared by all objects of a class (static).
# 2. **Properties**:
#    - Provide getter, setter, and deleter methods for attribute control.
# 3. **Generic Types**:
#    - Allow you to define classes or functions that work with any data type using TypeVar and Generic.
# 4. **Static vs Non-static State**:
#    - Static State: Shared across all instances of the class.
#    - Non-static State: Unique to each instance.
