# ============================================
#           OBJECT-ORIENTED PROGRAMMING
# ============================================

# 1. CLASSES AND OBJECTS
print("=== Classes and Objects ===")

# A class is a blueprint for creating objects (instances).
class Person:
    # Constructor (__init__ method) initializes object attributes.
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

    # Method: A function defined in a class
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Creating objects (instances) of the class
person1 = Person("Nagi", 20)
person2 = Person("Ammulu", 18)

# Accessing attributes and methods
print(person1.introduce())  # Output: My name is Nagi and I am 20 years old.
print(person2.introduce())  # Output: My name is Ammulu and I am 18 years old.

# ---------------------------------------------------------

# 2. INHERITANCE
print("\n=== Inheritance ===")

# Inheritance allows a class to inherit attributes and methods from another class.
class Student(Person):  # Student class inherits from Person
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)  # Call the parent class's constructor
        self.roll_number = roll_number  # New attribute

    def display(self):
        return f"{self.introduce()} My roll number is {self.roll_number}."

student = Student("Nagi", 20, 101)
print(student.display())  # Output: My name is Nagi and I am 20 years old. My roll number is 101.

# ---------------------------------------------------------

# 3. POLYMORPHISM
print("\n=== Polymorphism ===")

# Polymorphism allows the same method name to behave differently in different classes.
class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

# Function demonstrating polymorphism
def animal_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!

# ---------------------------------------------------------

# 4. ENCAPSULATION
print("\n=== Encapsulation ===")

# Encapsulation is the practice of restricting direct access to attributes or methods.
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance  # Getter method for private attribute

account = BankAccount("Nagi", 1000)
account.deposit(500)  # Deposited 500. New balance: 1500
account.withdraw(200)  # Withdrew 200. New balance: 1300
print(account.get_balance())  # Output: 1300
# Note: Direct access to `__balance` is not allowed (encapsulation).

# ---------------------------------------------------------

# 5. ABSTRACTION
print("\n=== Abstraction ===")

# Abstraction is achieved using abstract base classes (ABC) in Python.
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract Base Class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

rectangle = Rectangle(10, 5)
print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 50
print(f"Rectangle Perimeter: {rectangle.perimeter()}")  # Output: Rectangle Perimeter: 30

# ---------------------------------------------------------

# 6. SPECIAL METHODS (DUnder or Magic Methods)
print("\n=== Special Methods ===")

# Special methods are predefined methods with double underscores (e.g., __init__, __str__).
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point1 = Point(2, 3)
point2 = Point(4, 5)
print(point1)  # Output: Point(2, 3)
print(point1 + point2)  # Output: Point(6, 8)

# ---------------------------------------------------------

# 7. CLASS METHODS AND STATIC METHODS
print("\n=== Class Methods and Static Methods ===")

class Utility:
    counter = 0  # Class attribute

    @classmethod
    def increment_counter(cls):
        cls.counter += 1

    @staticmethod
    def greet(name):
        return f"Hello, {name}!"

Utility.increment_counter()
Utility.increment_counter()
print(f"Counter: {Utility.counter}")  # Output: Counter: 2
print(Utility.greet("Nagi"))  # Output: Hello, Nagi!

# ---------------------------------------------------------

# 8. MULTIPLE INHERITANCE
print("\n=== Multiple Inheritance ===")

class Parent1:
    def method1(self):
        return "Parent1 Method"

class Parent2:
    def method2(self):
        return "Parent2 Method"

class Child(Parent1, Parent2):
    def method3(self):
        return "Child Method"

child = Child()
print(child.method1())  # Output: Parent1 Method
print(child.method2())  # Output: Parent2 Method
print(child.method3())  # Output: Child Method
