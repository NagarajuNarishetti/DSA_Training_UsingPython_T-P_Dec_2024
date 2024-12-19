# ============================================
#                CONSTRUCTORS IN PYTHON
# ============================================

"""
Theory:
1. A **constructor** is a special method in Python that is automatically invoked when an object is created from a class.
2. The constructor is defined using the `__init__` method.
3. The primary use of the constructor is to initialize the object's attributes.
4. The constructor receives at least one argument (`self`), which is a reference to the current instance of the class.
5. You can pass additional arguments to the constructor to initialize instance variables.
6. If no constructor is provided, Python uses a default constructor.
"""

# Example 1: Basic Constructor
print("=== Example 1: Basic Constructor ===")

class Person:
    # Constructor with parameters to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Initialize instance variable 'name'
        self.age = age    # Initialize instance variable 'age'

    # Method to display object information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects of the class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing the display_info method to print details of the objects
person1.display_info()  # Output: Name: Alice, Age: 30
person2.display_info()  # Output: Name: Bob, Age: 25

# ---------------------------------------------------------

# Example 2: Default Constructor
print("\n=== Example 2: Default Constructor ===")

class Animal:
    # Default constructor (implicitly provided by Python)
    def __init__(self):
        self.name = "Unknown"  # Default value
        self.species = "Unknown"  # Default value

    # Method to display object information
    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}")

# Creating an object with the default constructor
animal1 = Animal()
animal1.display_info()  # Output: Name: Unknown, Species: Unknown

# ---------------------------------------------------------

# Example 3: Constructor with Default Arguments
print("\n=== Example 3: Constructor with Default Arguments ===")

class Book:
    # Constructor with default arguments for title and author
    def __init__(self, title="Unknown", author="Unknown"):
        self.title = title
        self.author = author

    # Method to display object information
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

# Creating an object with default values
book1 = Book()
book1.display_info()  # Output: Title: Unknown, Author: Unknown

# Creating an object with custom values
book2 = Book("1984", "George Orwell")
book2.display_info()  # Output: Title: 1984, Author: George Orwell

# ---------------------------------------------------------

# Example 4: Modifying Attributes Using Constructor
print("\n=== Example 4: Modifying Attributes Using Constructor ===")

class Car:
    # Constructor to initialize the attributes of the car
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    # Method to display car details
    def display_info(self):
        print(f"{self.color} {self.brand} {self.model}")

# Creating car objects with custom attributes
car1 = Car("Toyota", "Corolla", "Red")
car2 = Car("Tesla", "Model S", "Black")

# Accessing the display_info method to print details of the cars
car1.display_info()  # Output: Red Toyota Corolla
car2.display_info()  # Output: Black Tesla Model S

# ---------------------------------------------------------

# Example 5: The `self` Keyword in Constructor
print("\n=== Example 5: The `self` Keyword in Constructor ===")

class Student:
    # Constructor with parameters for name and grade
    def __init__(self, name, grade):
        self.name = name  # 'self' is used to refer to the object instance
        self.grade = grade

    # Method to display student's info
    def display_info(self):
        print(f"Student: {self.name}, Grade: {self.grade}")

# Creating objects of the Student class
student1 = Student("Alice", "A")
student2 = Student("Bob", "B")

# Accessing the display_info method to print student details
student1.display_info()  # Output: Student: Alice, Grade: A
student2.display_info()  # Output: Student: Bob, Grade: B

"""
Theory Notes:
- The `self` parameter in the constructor (and other methods) refers to the current instance of the class.
- `self` allows you to access and modify attributes that belong to the instance of the object.
- The constructor is automatically called when an object is instantiated.
- You can define default values for parameters in the constructor, making them optional when creating objects.
"""

# Final Output Message
print("\n--- Constructors in Python Examples Complete ---")
