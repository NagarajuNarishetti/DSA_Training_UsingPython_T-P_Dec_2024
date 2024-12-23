# Demonstrating Operator Overloading in Python

class Point:
    """
    A class representing a point in 2D space.
    Demonstrates operator overloading for basic arithmetic operations.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Overloads the '+' operator to add two Point objects.
        """
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        raise TypeError("Operand must be an instance of Point")

    def __sub__(self, other):
        """
        Overloads the '-' operator to subtract one Point object from another.
        """
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        raise TypeError("Operand must be an instance of Point")

    def __mul__(self, scalar):
        """
        Overloads the '*' operator to multiply a Point object by a scalar.
        """
        if isinstance(scalar, (int, float)):
            return Point(self.x * scalar, self.y * scalar)
        raise TypeError("Operand must be an int or float")

    def __eq__(self, other):
        """
        Overloads the '==' operator to compare two Point objects for equality.
        """
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        """
        Returns a string representation of the Point object.
        """
        return f"Point({self.x}, {self.y})"

# Examples demonstrating operator overloading
if __name__ == "__main__":
    print("=== Operator Overloading Example ===")
    
    # Creating two Point objects
    p1 = Point(2, 3)
    p2 = Point(4, 5)

    print(f"Point 1: {p1}")  # Output: Point 1: Point(2, 3)
    print(f"Point 2: {p2}")  # Output: Point 2: Point(4, 5)

    # Adding two Point objects
    p3 = p1 + p2  # Calls __add__
    print(f"Addition (p1 + p2): {p3}")  # Output: Addition (p1 + p2): Point(6, 8)

    # Subtracting two Point objects
    p4 = p1 - p2  # Calls __sub__
    print(f"Subtraction (p1 - p2): {p4}")  # Output: Subtraction (p1 - p2): Point(-2, -2)

    # Multiplying a Point object by a scalar
    p5 = p1 * 3  # Calls __mul__
    print(f"Multiplication (p1 * 3): {p5}")  # Output: Multiplication (p1 * 3): Point(6, 9)

    # Comparing two Point objects for equality
    print(f"Equality (p1 == p2): {p1 == p2}")  # Output: Equality (p1 == p2): False
    print(f"Equality (p1 == Point(2, 3)): {p1 == Point(2, 3)}")  # Output: Equality (p1 == Point(2, 3)): True
