# 1. Defining and Calling a Function
def greet():
    print("Hello, welcome to Python functions!")  # Output: Hello, welcome to Python functions!

greet()

# 2. Functions with Parameters
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python functions.")  # Output: Hello, Nagi! Welcome to Python functions.

greet_user("Nagi")

# 3. Functions with Return Values
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print(f"The sum is: {result}")  # Output: The sum is: 30

# 4. Default Arguments
def greet(name="User"):
    print(f"Hello, {name}!")  # Output: Hello, User! (default), Hello, Nagi!

greet()       
greet("Nagi") 

# 5. Keyword Arguments
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")  # Output: Name: Nagi, Age: 20

display_info(age=20, name="Nagi")

# 6a. Variable-Length Arguments (*args)
def add_all(*numbers):
    return sum(numbers)

print(f"Sum of numbers: {add_all(1, 2, 3, 4, 5)}")  # Output: Sum of numbers: 15

# 6b. Variable-Length Keyword Arguments (**kwargs)
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")  # Output: name: Nagi, age: 20, city: Hyderabad

show_profile(name="Nagi", age=20, city="Hyderabad")

# 7. Lambda Functions
square = lambda x: x * x
print(f"Square of 5 is: {square(5)}")  # Output: Square of 5 is: 25

numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")  # Output: Squared numbers: [1, 4, 9, 16]

# 8a. Passing Functions as Arguments
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func, text):
    print(func(text))  # Output: HELLO, hello

greet(shout, "hello")
greet(whisper, "HELLO")

# 8b. Returning Functions
def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
print(f"Double of 5 is: {double(5)}")  # Output: Double of 5 is: 10

# 9. Recursive Functions
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5 is: {factorial(5)}")  # Output: Factorial of 5 is: 120

# 10. Scope and Lifetime of Variables
x = "global"

def my_function():
    x = "local"
    print(f"Inside function: {x}")  # Output: Inside function: local

my_function()
print(f"Outside function: {x}")  # Output: Outside function: global

# Using `global` Keyword
count = 0

def increment():
    global count
    count += 1

increment()
print(f"Global count: {count}")  # Output: Global count: 1

# 11. Docstrings in Functions
def greet(name):
    """This function greets the person whose name is passed."""
    print(f"Hello, {name}!")  # Output: Hello, Nagi!

print(greet.__doc__)  # Output: This function greets the person whose name is passed.

# 12. Decorators
def decorator(func):
    def wrapper():
        print("Before the function call")  # Output: Before the function call
        func()  # Output: Hello!
        print("After the function call")  # Output: After the function call
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# 13. Built-in Higher-Order Functions
numbers = [1, 2, 3, 4]

# map()
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled numbers: {doubled}")  # Output: Doubled numbers: [2, 4, 6, 8]

# filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")  # Output: Even numbers: [2, 4]

# reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of numbers: {product}")  # Output: Product of numbers: 24
