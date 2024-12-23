'''class Student:
    name="varma"
    def printName(self,n):
        print(n)

v=Student()
v1=Student
print(v.name)
print(v.printName("Nagi"))
print(id(v))
print(id(v1))'''

# ============================================
#              CLASSES AND OBJECTS
# ============================================

"""
Theory:
1. A **class** is a blueprint for creating objects.
   - It defines properties (attributes) and behaviors (methods) that the objects will have.
   - Classes allow organizing code into reusable and logical components.

2. An **object** is an instance of a class.
   - Objects hold data (attributes) and use methods to perform operations.

Syntax for a Class:
class ClassName:
    def __init__(self, attributes):
        # Initialize attributes (constructor)

    def method_name(self):
        # Define behaviors (methods)
"""

# Example 1: Defining a Class and Creating an Object
print("=== Example 1: Class and Object ===")

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand  # Attribute
        self.model = model
        self.color = color

    def drive(self):  # Method
        return f"{self.color} {self.brand} {self.model} is driving."

# Create an object of the class
car1 = Car("Toyota", "Corolla", "Red")
car2 = Car("Tesla", "Model S", "Black")

# Access attributes and methods
print(car1.drive())  # Output: Red Toyota Corolla is driving.
print(car2.drive())  # Output: Black Tesla Model S is driving.

# ---------------------------------------------------------

# Example 2: Attributes and Methods
print("\n=== Example 2: Attributes and Methods ===")

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def is_pass(self):
        return self.marks >= 40  # Returns True if marks >= 40

student1 = Student("Alice", 101, 85)
student2 = Student("Bob", 102, 35)

print(f"{student1.name} Pass Status: {student1.is_pass()}")  # Output: Alice Pass Status: True
print(f"{student2.name} Pass Status: {student2.is_pass()}")  # Output: Bob Pass Status: False

# ---------------------------------------------------------

# Example 3: Modifying Attributes
print("\n=== Example 3: Modifying Attributes ===")

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def update_price(self, new_price):
        self.price = new_price

    def book_info(self):
        return f"'{self.title}' by {self.author}, priced at ${self.price}"

book = Book("The Alchemist", "Paulo Coelho", 20)
print(book.book_info())  # Output: 'The Alchemist' by Paulo Coelho, priced at $20
book.update_price(18)
print(book.book_info())  # Output: 'The Alchemist' by Paulo Coelho, priced at $18

# ---------------------------------------------------------

# Example 4: Class vs Instance Attributes
print("\n=== Example 4: Class vs Instance Attributes ===")

class Counter:
    # Class attribute
    count = 0

    def __init__(self, name):
        self.name = name  # Instance attribute
        Counter.count += 1  # Increment class attribute for each object created

counter1 = Counter("First Counter")
counter2 = Counter("Second Counter")
print(f"Total Counters: {Counter.count}")  # Output: Total Counters: 2
print(f"Name of counter1: {counter1.name}")  # Output: Name of counter1: First Counter

# ---------------------------------------------------------

# Example 5: The `self` Keyword
print("\n=== Example 5: The self Keyword ===")

class Example:
    def __init__(self, value):
        self.value = value

    def update_value(self, new_value):
        self.value = new_value

    def show_value(self):
        return f"The current value is {self.value}"

example = Example(10)
print(example.show_value())  # Output: The current value is 10
example.update_value(20)
print(example.show_value())  # Output: The current value is 20

"""
Theory:
- The `self` keyword represents the current instance of the class.
- It is used to access attributes and methods of the object.
"""

# ---------------------------------------------------------

# Example 6: Object Methods vs Static Methods
print("\n=== Example 6: Object Methods vs Static Methods ===")

class Math:
    def square(self, x):  # Instance method
        return x * x

    @staticmethod
    def cube(x):  # Static method
        return x * x * x

math = Math()
print(math.square(4))  # Output: 16 (Instance method)
print(Math.cube(3))    # Output: 27 (Static method)

"""
Theory:
- Instance methods use the `self` parameter and can access instance attributes.
- Static methods do not require `self` and can be called without creating an object.
"""

# ---------------------------------------------------------

# Example 7: Object Destruction
print("\n=== Example 7: Object Destruction ===")

class Demo:
    def __init__(self, name):
        self.name = name

    def __del__(self):  # Destructor method
        print(f"{self.name} is being deleted.")

demo1 = Demo("Demo1")
demo2 = Demo("Demo2")
del demo1  # Output: Demo1 is being deleted.

"""
Theory:
- Destructors (`__del__`) are called when an object is deleted or goes out of scope.
"""

# ---------------------------------------------------------

# Theory Summary:
"""
1. **Class**: A blueprint defining the attributes (data) and methods (behavior) of objects.
2. **Object**: An instance of a class that holds actual data and performs operations using methods.
3. **Attributes**: Variables defined in a class. They can be instance-specific or shared across the class.
4. **Methods**: Functions inside a class that define behaviors of objects.
5. **self**: Refers to the current object and is used to access attributes and methods.
6. **Constructor (`__init__`)**: Initializes attributes when an object is created.
7. **Destructor (`__del__`)**: Cleans up resources or performs final actions before the object is destroyed.
8. **Static Methods**: Methods that don't depend on object-specific data.
"""

# Final Output:
print("\n--- Classes and Objects Examples Complete ---")
