# ============================================
#                INHERITANCE & CONSTRUCTORS
# ============================================

"""
Theory:
1. Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
2. The constructor of the parent class can be inherited by the child class, but the child class can also have its own constructor.
3. We can call the parent class's constructor explicitly using `super()` if we need to initialize the parent class's attributes.
4. The `__init__` method in the parent class is used to initialize the parent's attributes, and the child class can call this to initialize both parent and child attributes.
"""

# Example 1: Parent and Child Class with Constructors
print("=== Example 1: Parent and Child Class with Constructors ===")

# Parent Class
class Animal:
    # Constructor in the parent class
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Method to display animal information
    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}")

# Child Class inheriting from Parent Class
class Dog(Animal):
    # Constructor in the child class
    def __init__(self, name, species, breed):
        # Call the parent class constructor to initialize parent attributes
        super().__init__(name, species)  
        self.breed = breed  # Initialize child-specific attribute

    # Method to display dog-specific information
    def display_info(self):
        # Call the parent class method to display parent attributes
        super().display_info()
        print(f"Breed: {self.breed}")

# Creating an object of the child class
dog1 = Dog("Rex", "Canine", "German Shepherd")

# Accessing the display_info method of the child class
dog1.display_info()  
# Output: 
# Name: Rex, Species: Canine
# Breed: German Shepherd

# ---------------------------------------------------------

# Example 2: Parent Class Constructor Initialization
print("\n=== Example 2: Parent Class Constructor Initialization ===")

# Parent Class
class Vehicle:
    # Constructor in the parent class
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}")

# Child Class inheriting from Parent Class
class Car(Vehicle):
    # Constructor in the child class
    def __init__(self, make, model, year):
        # Call the parent class constructor using super()
        super().__init__(make, model)
        self.year = year

    # Method to display car-specific information
    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")

# Creating objects of the child class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Tesla", "Model 3", 2023)

# Displaying details of the vehicles (parent + child attributes)
car1.display_info()  
# Output: 
# Vehicle Make: Toyota, Model: Camry
# Year: 2020

car2.display_info()  
# Output:
# Vehicle Make: Tesla, Model: Model 3
# Year: 2023

# ---------------------------------------------------------

# Example 3: Child Class Constructor Without Parent Constructor
print("\n=== Example 3: Child Class Constructor Without Parent Constructor ===")

# Parent Class
class Bird:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Bird Name: {self.name}")

# Child Class without calling the parent constructor
class Parrot(Bird):
    def __init__(self, name, color):
        self.color = color
        self.name = name  # Explicitly assigning parent's attribute

    def display_info(self):
        print(f"Parrot Name: {self.name}, Color: {self.color}")

# Creating an object of the Parrot class
parrot1 = Parrot("Polly", "Green")
parrot1.display_info()  
# Output: Parrot Name: Polly, Color: Green

"""
Theory Notes:
1. **Inheritance** allows a child class to inherit methods and attributes from a parent class.
2. **super()** is used to call the parent class constructor or methods from the child class.
3. In Example 1, the child class `Dog` inherits from the parent class `Animal`, and it uses `super()` to call the constructor of the parent class to initialize the `name` and `species` attributes.
4. In Example 2, `Car` inherits from `Vehicle`, and the constructor of `Vehicle` is called using `super()` to initialize the `make` and `model` of the car.
5. In Example 3, the child class `Parrot` doesn't call the parent constructor but still assigns the parent attribute manually in the constructor.

In summary, the **constructor** in Python plays a crucial role in object initialization, and inheritance allows the child class to either use or modify the behavior of the parent class constructor.
"""

# Final Output Message
print("\n--- Inheritance and Constructors Examples Complete ---")
