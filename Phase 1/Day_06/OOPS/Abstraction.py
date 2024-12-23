# Astraction 
'''
-The process of hiding the information/conplixty of features and exposing only features/functionality to end users is called as abstarcation 
-# how  to achive abstartion 
    -declaring  all mathods and varibles in class with abstact method dedcorator 
    - we shoud import abc(abstact base class) module and ABC class
    -Abstact method decorator
-For abstact method if there is not implimatain it will throw erro 
-For all the abstact methods which we declare in a class we need to provide pass as an implimentation in the function 
-# Note:
 -Clild calss is reponsible for poviding implimatatoin for parent classs abstract method

 # Abstract Method
    -If we did 't provide implimataion for a function it will give an error so to avoid the error we need to provide pass key word in the implimentation
    - In order to provide a strucute for a class/All subclasses we need abstraction 
 
 '''





from abc import ABC, abstractmethod

# Python Abstraction Demonstration

# Abstract Class (Abstract Base Class)
class Shape(ABC):  # Inheriting from ABC to make this class abstract
    def __init__(self):
        # Abstract class can have constructor
        self.name = "Shape"
    
    # Abstract method (must be implemented by any subclass)
    @abstractmethod
    def area(self):
        pass
    
    # Regular method (concrete method) - Can be used directly by subclasses
    def display_name(self):
        print(f"This is a {self.name}.")

# Concrete class that implements the abstract method
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.name = "Circle"
    
    # Implementation of abstract method
    def area(self):
        return 3.14 * self.radius * self.radius  # Formula for area of circle

# Concrete class that implements the abstract method
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.name = "Rectangle"
    
    # Implementation of abstract method
    def area(self):
        return self.length * self.width  # Formula for area of rectangle

# Creating objects of concrete classes
circle = Circle(5)  # Circle with radius 5
rectangle = Rectangle(4, 6)  # Rectangle with length 4 and width 6

# Accessing methods from concrete class
print(f"Area of {circle.name}: {circle.area()}")  # Output area of circle
circle.display_name()  # Output name of the shape

print(f"Area of {rectangle.name}: {rectangle.area()}")  # Output area of rectangle
rectangle.display_name()  # Output name of the shape

# Trying to create an object of the abstract class directly
# This will raise an error because we cannot instantiate an abstract class
# shape = Shape()  # Uncommenting this line will raise TypeError: Can't instantiate abstract class Shape with abstract methods area

# Breakdown of Abstraction:

# 1. Abstract Class:
# An abstract class is a class that cannot be instantiated directly. It serves as a blueprint for other classes.
# In Python, we create an abstract class by inheriting from the ABC (Abstract Base Class) module and using the @abstractmethod decorator.
# Abstract classes can contain both abstract methods (which must be implemented by subclasses) and concrete methods (which can be inherited as-is by subclasses).

# 2. Abstract Method:
# Abstract methods are methods that are defined in an abstract class but do not have any implementation.
# Any subclass that inherits from an abstract class must implement all abstract methods of that class.

# 3. Concrete Class:
# A concrete class is a class that can be instantiated. It is derived from an abstract class and provides implementations for all abstract methods.
# Once the abstract methods are implemented in the concrete class, the class can be instantiated and used like any normal class.

# Advantages of Abstraction:
# - Hides complexity: It provides a way to define methods in an abstract class without exposing the implementation details.
# - Reduces coupling: It ensures that code does not rely on the internal implementation details of other classes.
# - Provides a clear structure: It enforces a contract for subclasses to follow by requiring them to implement abstract methods.
# - Code reusability: Concrete classes can inherit abstract classes and reuse code, while only implementing the abstract methods specific to the class.

# Example usage of the abstraction concept:
# - The Shape class provides a blueprint for different geometric shapes, but we don't know how the area is calculated until we implement that in specific subclasses like Circle and Rectangle.
# - The user of the classes can interact with the Shape class (via its concrete subclasses) without knowing how each shape calculates its area.

# To summarize:
# - Abstraction allows us to define general behavior in an abstract class and leave specific behavior to be implemented in concrete classes.
# - Abstract classes are not meant to be instantiated. They are used to provide a common interface for all subclasses.
# - Abstract methods must be implemented in concrete classes that inherit from an abstract class.
