# Python Access Specifiers - Public, Protected, Private


#Private
'''
-atributes and methods are accesable only with in the class
-They are gone reprasented by double underscore(__)
'''

# protected
'''
-Atibutes and Methods are only accesable with in the class and its subclasses it is reprasented by a single underscore (_)
'''
#Public 
'''
- The atributes or methods can be accesed inside the class and outside the class 
'''

# note:
'''
    -Techinically Noting prevents you form accesing the protected members directly it is a convention that indicates to other developers that thse membrers are invnted for intenal use 
'''

class MyClass:
    def __init__(self):
        # Public attribute
        self.public_var = "I am public"  # Public attribute - Accessible anywhere
        
        # Protected attribute (using a single underscore to indicate it's for internal use)
        self._protected_var = "I am protected"  # Protected attribute - Should be used within the class or its subclasses
        
        # Private attribute (using double underscore to enforce name mangling)
        self.__private_var = "I am private"  # Private attribute - Not accessible from outside the class
        
    # Public method
    def public_method(self):
        print("This is a public method.")
        print(f"Accessing public variable: {self.public_var}")
    
    # Protected method
    def _protected_method(self):
        print("This is a protected method.")
        print(f"Accessing protected variable: {self._protected_var}")
    
    # Private method
    def __private_method(self):
        print("This is a private method.")
        print(f"Accessing private variable: {self.__private_var}")
    
    # Method to demonstrate the access to protected and private members from within the class
    def access_protected_private(self):
        print("Accessing protected and private members from within the class:")
        print(f"Protected: {self._protected_var}")
        print(f"Private: {self.__private_var}")
    
# Creating an object of MyClass
obj = MyClass()

# 1. Accessing public attribute and method
print("Public access:")
print(obj.public_var)  # Direct access to public attribute
obj.public_method()    # Calling public method

# 2. Accessing protected attribute and method from outside the class
# This is allowed but not recommended. The protected attribute/method is meant for internal use.
print("\nProtected access:")
print(obj._protected_var)  # Accessing protected attribute directly (not recommended)
obj._protected_method()    # Accessing protected method directly (not recommended)

# 3. Accessing private attribute and method from outside the class
# This will raise an error, as private attributes and methods cannot be accessed directly.
# Uncommenting the lines below will raise an AttributeError
# print(obj.__private_var)  # This will raise AttributeError
# obj.__private_method()    # This will raise AttributeError

# 4. Accessing private attribute and method via name mangling
# Python does name mangling to make private members harder to access from outside the class.
print("\nPrivate access via name mangling:")
print(obj._MyClass__private_var)  # Accessing private variable via name mangling
obj._MyClass__private_method()    # Calling private method via name mangling

# 5. Accessing protected and private attributes from within the class using a method
print("\nAccessing protected and private from within the class:")
obj.access_protected_private()

# Demonstrating how subclasses can access protected and private members
class SubClass(MyClass):
    def __init__(self):
        super().__init__()

    def access_protected_from_subclass(self):
        # Accessing the protected variable and method inside subclass
        print("\nAccessing protected members from subclass:")
        print(self._protected_var)  # Accessing protected attribute in subclass
        self._protected_method()    # Accessing protected method in subclass

# Creating an object of SubClass
sub_obj = SubClass()

# Subclass can access protected attributes/methods but not private members
sub_obj.access_protected_from_subclass()

# To summarize:
# - Public: Accessible from anywhere (both inside and outside the class).
# - Protected: Intended for internal use within the class and its subclasses. Can be accessed but discouraged outside.
# - Private: Intended to be used only within the class. Python uses name mangling to make them less accessible from outside.

# Breakdown of Access Specifiers in Python:

# 1. Public Attributes and Methods:
# public_var is a public attribute that can be accessed from anywhere, both inside and outside the class.
# public_method() is a public method that can also be called from anywhere.

# 2. Protected Attributes and Methods:
# _protected_var is a protected attribute, and _protected_method() is a protected method. 
# While they can be accessed from subclasses, it is generally discouraged to access them from outside the class.

# 3. Private Attributes and Methods:
# __private_var is a private attribute, and __private_method() is a private method. 
# These members are not directly accessible outside the class. If you try to access them, it will result in an AttributeError.
# Name mangling: Python internally changes the names of private members by adding the class name as a prefix.
# This makes it harder (but not impossible) to access private members from outside the class.

# 4. Subclass Access:
# A subclass can access protected members but cannot directly access private members.

# Advantages:
# - Public members provide easy access to necessary data and functions.
# - Protected members help with data encapsulation by limiting access to only the class and its subclasses.
# - Private members ensure that sensitive data and internal methods are only accessible within the class itself.

# Best Practices:
# - Public members are used for data and methods that need to be accessed freely.
# - Protected members are used for attributes/methods that are intended for internal use, and if inherited, they can be used or modified in the subclass.
# - Private members should be used for attributes/methods that are strictly internal to the class and should not be modified or accessed from outside.
# Even though Python does not strictly enforce these access levels, it is still a good practice to use these conventions to maintain readability, consistency, and proper encapsulation of your code.
