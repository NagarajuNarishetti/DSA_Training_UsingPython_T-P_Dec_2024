# Filename: self_keyword_info.py

# Key Points About `self` in Python

"""
1. `self` is a reference to the current instance of the class.
2. It is the first parameter in instance methods, allowing them to access instance attributes and methods.
3. `self` is not a keyword in Python; it's just a naming convention.
4. It is used to differentiate between instance variables and local variables.

Usage of `self`:
- `self` allows methods to refer to and modify instance attributes.
- It enables access to other methods within the class.
- Helps in distinguishing between instance and class variables.

Example Usage:
"""

class Person:
    # Constructor with self parameter to initialize instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method using self to access attributes
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    
    # Instance method modifying an attribute using self
    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

# Creating an instance of Person
person1 = Person("Alice", 30)

# Calling instance methods that use `self`
person1.greet()          # Outputs: Hello, my name is Alice and I am 30 years old.
person1.have_birthday()  # Outputs: Happy Birthday, Alice! You are now 31 years old.

"""
Important Notes:

1. `self` is used to refer to the instance of the class, allowing methods to access and modify instance attributes.
2. Without `self`, Python wouldn't be able to differentiate between instance variables and local variables.
3. `self` can be named anything, but using `self` is a widely accepted convention that makes the code easier to read and maintain.
4. `self` is required in every instance method, as it makes the method aware of which instance it is working with.
5. When using inheritance, `self` works the same way, referring to the instance of the subclass.

Usage in Inheritance:
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

# Creating an instance of Dog
dog = Dog("Buddy")
dog.speak()  # Outputs: Buddy barks.

"""
Static and Class Methods (No `self`):
In static and class methods, `self` is not required as they don't operate on instance-specific data.

- Class Method (uses `cls` instead of `self`):
"""

class MyClass:
    class_var = 0

    @classmethod
    def increment_class_var(cls):
        cls.class_var += 1
        print(f"Class variable: {cls.class_var}")

MyClass.increment_class_var()  # Outputs: Class variable: 1

"""
- Static Method (doesn't require `self` or `cls`):
"""

class MyClass:
    @staticmethod
    def greet():
        print("Hello, this is a static method.")

MyClass.greet()  # Outputs: Hello, this is a static method.

"""
Conclusion:
- `self` is crucial for instance methods to access and modify instance-specific attributes.
- It is a convention, not a keyword, and can be named anything, but `self` is preferred for clarity.
- In static and class methods, `self` is not used, as these methods don't rely on instance-specific data.

"""

# Save this file for future reference and push it to your GitHub repository for future use.
