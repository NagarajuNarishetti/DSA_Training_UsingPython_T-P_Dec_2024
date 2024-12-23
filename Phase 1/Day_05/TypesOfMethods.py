# Filename: methods_types_info.py

# Key Points About Three Types of Methods in Python

"""
In Python, there are three main types of methods that can be defined within a class:
1. Instance (Object) Methods
2. Class Methods
3. Static Methods

### 1. Instance (Object) Methods:
-Default type of a method when you deifne a method in a class is instace method
- Instance methods are the most common type of methods in Python.
- They require an instance (or object) of the class to be called.
- They take `self` as the first argument, which refers to the instance calling the method.

Usage:
- Instance methods are used to access or modify instance attributes and call other instance methods.
- These methods are designed to operate on individual instances of the class.

Example:

"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    # Instance method modifying an instance attribute
    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Creating an instance of Person
person1 = Person("Alice", 30)

# Calling instance methods
person1.greet()          # Outputs: Hello, my name is Alice and I am 30 years old.
person1.have_birthday()  # Outputs: Happy Birthday, Alice! You are now 31 years old.

"""
### 2. Class Methods:
- Class methods are defined using the `@classmethod` decorator.
- They require the class itself as the first argument, which is usually named `cls`.
- Class methods can be called on the class itself, without creating an instance.

Usage:
- Class methods are used to operate on class-level attributes.
- They can modify class variables or perform tasks related to the class itself, not specific to an instance.
-They are perticulerly useful when you need to modify or set calss varibles shared by all instace of the class
-class methods do not have acesess to instace specific data or instace attributes 

**** Indirect way to create a class  instace(constructor) ****
    __init__
    this is a special method in python class that is called when a new instance of the class is created
    -it inializes the instance varibles of the class 

**** 2nd Method ****
    Iterretor class metod 
    this is a decorator in pytohn used to define a method that operatos on a class itself rathor than instace of the class and in this u can use cls to refer itslef which helps us to create new instace of a class
Example:
"""

class SRU:
    a=10
    @classmethod
    def display(cls):
        print(cls.a," before Modify")
    @classmethod
    def modify(cls,num):
        cls.a=num
        print(cls.a," after modify")
s=SRU
s.display()
s.modify(189)

class Animal:
    species = "Unknown"  # A class-level attribute

    def __init__(self, name):
        self.name = name

    # Class method
    @classmethod
    def set_species(cls, species):
        cls.species = species

    @classmethod
    def get_species(cls):
        return cls.species

# Calling class methods without creating an instance
Animal.set_species("Dog")
print(Animal.get_species())  # Outputs: Dog

# Creating an instance of Animal
dog = Animal("Buddy")
print(dog.name)  # Outputs: Buddy
print(dog.get_species())  # Outputs: Dog (class-level attribute)

"""
### 3. Static Methods:
- Static methods are defined using the `@staticmethod` decorator.
- Static methods do not take `self` or `cls` as the first argument.
- They are independent of both instance and class-level data.
- Static methods are used when a method does not need to modify or access instance or class attributes.

Usage:
- Static methods are used to perform utility functions or tasks that do not rely on the state of the class or instance.


Example:
"""

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# Calling static methods without creating an instance
print(MathUtils.add(5, 3))        # Outputs: 8
print(MathUtils.multiply(5, 3))   # Outputs: 15

"""
### Summary:
1. **Instance Method**: Requires an instance of the class and uses `self`. It operates on instance-specific data.
2. **Class Method**: Requires the class itself as the first argument (`cls`). It operates on class-level data.
3. **Static Method**: Does not require `self` or `cls`. It is independent of instance and class-specific data and can be used for utility functions.

"""

# Save this file for future reference and push it to your GitHub repository for future use.
