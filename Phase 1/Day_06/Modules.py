



# Python Modules Demonstration

# Let's assume we have two files:
# 1. math_operations.py (A module that contains functions)
# 2. main.py (A script that imports and uses the module)

# math_operations.py (This would be a separate file, just like an external module)
# Saving this file as 'math_operations.py'


def add(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first and returns the result.
    """
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    """
    return a * b

def divide(a, b):
    """
    Divides the first number by the second and returns the result.
    If division by zero is attempted, it returns an error message.
    """
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# main.py (This would be another Python script where we import the module)

# Importing the custom math_operations module
import math_operations

# Using the functions from the math_operations module
a = 10
b = 5

# Addition
result = math_operations.add(a, b)
print(f"{a} + {b} = {result}")

# Subtraction
result = math_operations.subtract(a, b)
print(f"{a} - {b} = {result}")

# Multiplication
result = math_operations.multiply(a, b)
print(f"{a} * {b} = {result}")

# Division
result = math_operations.divide(a, b)
print(f"{a} / {b} = {result}")

# Alternative Importing Method: Import specific functions
from math_operations import add, subtract

# Now we can directly use add and subtract without using the module name
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {subtract(a, b)}")

# Alternative Importing Method: Import with alias
import math_operations as mo

# Using the alias 'mo' to access functions
print(f"{a} * {b} = {mo.multiply(a, b)}")
print(f"{a} / {b} = {mo.divide(a, b)}")


# Breakdown of Modules:

# 1. What is a Module in Python:
# A module is a file that contains Python definitions and statements. The file name is the module name with the suffix .py added.
# Modules are used to organize and structure code logically. By using modules, we can group related functions, classes, or variables into a single file, making the code easier to maintain and reuse.

# 2. How to Create a Module:
# A module is simply a Python file (.py) containing functions, variables, and classes.
# For example, in this case, 'math_operations.py' is a module, and it contains several mathematical operations like add, subtract, multiply, and divide.

# 3. How to Use a Module:
# Once a module is created, you can use it in other Python scripts or files by importing it using the `import` statement.
# There are different ways to import:
# - `import module_name` allows access to all functions in the module via the module's name.
# - `from module_name import function_name` allows you to import specific functions directly, so you don't need to use the module name to access them.
# - `import module_name as alias` allows you to import the module with a shorter name (alias).

# 4. Why Use Modules:
# - **Code organization**: Modules help in grouping related code together, making it easier to manage large codebases.
# - **Code reusability**: Once a module is created, it can be reused in multiple projects or scripts.
# - **Namespace management**: Modules help in avoiding name conflicts by providing namespaces. This means you can have functions or variables with the same name in different modules.
# - **Encapsulation**: Modules allow you to encapsulate functionality and expose only the necessary parts of the code, hiding the implementation details.

# 5. Python Standard Library Modules:
# Python comes with a vast collection of built-in modules known as the Python Standard Library. These modules provide functionalities like file handling, regular expressions, networking, and more.
# Examples include:
# - `os` for interacting with the operating system
# - `math` for mathematical operations
# - `datetime` for working with dates and times
# - `random` for generating random numbers

# 6. Advantages of Using Modules:
# - **Modular Code**: Code becomes modular, making it easier to maintain and scale.
# - **Easier Debugging**: Since code is broken into smaller chunks (modules), it's easier to test and debug each module independently.
# - **Better Collaboration**: Multiple developers can work on different modules without interfering with each other's work.
# - **Avoids Duplication**: Code written in one module can be reused in different projects or parts of the project, preventing duplication of effort.
# - **Performance Optimization**: Python allows lazy loading of modules. A module is loaded into memory only when it's actually imported, improving performance.

# Summary of Modules:
# - A module is a file containing Python code (functions, classes, variables) that can be imported and reused in other programs.
# - Modules allow for code organization, encapsulation, and reusability.
# - You can import modules using `import`, `from ... import`, or with an alias.
# - Python’s standard library provides built-in modules that offer a wide range of functionalities.
