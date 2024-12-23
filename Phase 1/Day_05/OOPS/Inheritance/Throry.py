# Filename: inheritance_info.py

# Key Points About Inheritance in Python

"""
Inheritance is a fundamental concept in Object-Oriented Programming (OOP) that allows one class to inherit the attributes and methods of another class.
This allows code reusability and establishes a relationship between parent (base) and child (derived) classes.

### Key Concepts:
1. **Parent Class (Base Class)**: The class whose properties and methods are inherited by another class.
2. **Child Class (Derived Class)**: The class that inherits from the parent class and can add or modify the inherited properties and methods.
3. **Method Overriding**: In the child class, methods from the parent class can be overridden to provide specific functionality.
4. **Access to Parent Class Methods**: The child class can call methods from the parent class using `super()`.

### 1. Single Inheritance:
   A class inherits from one parent class.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inherits from Animal class
class Dog(Animal):
    def speak(self):  # Overriding the parent class method
        print(f"{self.name} barks.")

# Creating an instance of Dog
dog = Dog("Buddy")
dog.speak()  # Outputs: Buddy barks.

"""
In the example above:
- `Dog` inherits from `Animal`.
- The `speak` method is overridden in the `Dog` class to provide specific functionality for dogs.
- We create an instance of `Dog`, and it calls the overridden `speak` method.

### 2. Multiple Inheritance:
   A class inherits from more than one parent class.
"""

class Flyer:
    def fly(self):
        print("Flying in the sky.")

class Swimmer:
    def swim(self):
        print("Swimming in the water.")

# Child class inherits from both Flyer and Swimmer
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quacking!")

# Creating an instance of Duck
duck = Duck()
duck.fly()    # Outputs: Flying in the sky.
duck.swim()   # Outputs: Swimming in the water.
duck.quack()  # Outputs: Quacking!

"""
In this example:
- `Duck` inherits from both `Flyer` and `Swimmer`.
- The `Duck` class has access to methods from both `Flyer` and `Swimmer`.

### 3. Multilevel Inheritance:
   A class is derived from another derived class.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Mammal(Animal):
    def walk(self):
        print(f"{self.name} walks on land.")

class Dog(Mammal):
    def speak(self):  # Overriding the parent class method
        print(f"{self.name} barks.")

# Creating an instance of Dog
dog = Dog("Buddy")
dog.speak()  # Outputs: Buddy barks.
dog.walk()   # Outputs: Buddy walks on land.

"""
In this example:
- `Dog` inherits from `Mammal`, and `Mammal` inherits from `Animal`.
- The `speak` method is overridden in the `Dog` class, and the `walk` method is inherited from `Mammal`.

### 4. Hierarchical Inheritance:
   Multiple classes inherit from the same parent class.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} meows.")

# Creating instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")
dog.speak()  # Inherited from Animal
dog.bark()   # Defined in Dog
cat.speak()  # Inherited from Animal
cat.meow()   # Defined in Cat

"""
In this example:
- `Dog` and `Cat` inherit from `Animal`.
- Both classes can use the `speak` method inherited from `Animal` and define their own specific methods.

### 5. Hybrid Inheritance:
   A combination of more than one type of inheritance.
"""

class Animal:
    def speak(self):
        print("Animal speaks")

class Swimmer:
    def swim(self):
        print("Swimming")

class Mammal(Animal):
    def walk(self):
        print("Mammal walks")

class Whale(Swimmer, Mammal):
    def swim(self):
        print("Whale swims")

# Creating an instance of Whale
whale = Whale()
whale.speak()  # Inherited from Animal
whale.swim()   # Inherited from Swimmer and overridden in Whale
whale.walk()   # Inherited from Mammal

"""
In this example:
- `Whale` inherits from both `Swimmer` and `Mammal`.
- It demonstrates hybrid inheritance by combining different types of inheritance.

### Conclusion:
- **Inheritance** allows a class to inherit the properties and methods of another class.
- It promotes **code reusability** and makes it easier to maintain and modify code.
- **Method overriding** allows child classes to change or extend the behavior of inherited methods.
- `super()` is used to call methods from the parent class.

"""

