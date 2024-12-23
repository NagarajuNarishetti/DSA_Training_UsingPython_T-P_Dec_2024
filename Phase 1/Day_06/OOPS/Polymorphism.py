# Polymorphism Demonstration in Python

# Parent Class (Base Class)
class Animal:
    def make_sound(self):
        # Default implementation for a generic animal sound
        print("Some generic animal sound")

# Subclass (Dog)
class Dog(Animal):
    def make_sound(self):
        # Overriding the parent class method to give a dog sound
        print("Woof! Woof!")

# Subclass (Cat)
class Cat(Animal):
    def make_sound(self):
        # Overriding the parent class method to give a cat sound
        print("Meow! Meow!")

# Polymorphism in action: Using the same method name to make different sounds
def animal_sound(animal):
    # Calls the appropriate method based on the object type (Polymorphism)
    animal.make_sound()

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the function with different types of objects
print("Dog sound:")
animal_sound(dog)  # Output: Woof! Woof!

print("Cat sound:")
animal_sound(cat)  # Output: Meow! Meow!

# Explanation:
# In this example, we demonstrate Polymorphism, a fundamental concept of Object-Oriented Programming.
# - The base class Animal has a method make_sound() which is intended to be overridden by subclasses.
# - Both Dog and Cat are subclasses of Animal. Each subclass overrides the make_sound() method to provide its own specific sound.
# - The function animal_sound() accepts any object of type Animal. It calls the make_sound() method, which can vary depending on whether the object passed is a Dog or a Cat.
# - This is polymorphism in action, where the same method name `make_sound()` behaves differently depending on the type of object.

# Key Concepts of Polymorphism:
# 1. Method Overriding: A subclass can provide its specific implementation of a method that was already defined in the parent class.
# 2. Runtime Polymorphism: The method to be executed is determined at runtime based on the object type (Dog or Cat in this case).
# 3. Flexibility: You can use the same method name for different types of objects, and the correct method will be called depending on the object type.
# 4. Extensibility: You can add more subclasses (like `Bird`, `Lion`, etc.) in the future that also override the make_sound() method without changing the existing code.

# Advantages of Polymorphism:
# - Allows code to be more flexible and reusable by using the same method name for different objects.
# - Helps to write cleaner, more readable code as behavior is associated with the object type and not the method.
# - Makes it easier to extend the code, as new classes can be added without modifying the existing ones.

