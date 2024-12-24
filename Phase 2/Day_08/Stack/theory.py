# Stack Implementation and Theory in Python

# Theory:
# A stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
# The element added last is the first one to be removed.
# Common operations include:
# - push: Adding an element to the top of the stack.
# - pop: Removing the top element of the stack.
# - peek: Viewing the top element without removing it.
# - is_empty: Checking if the stack is empty.
# - size: Getting the number of elements in the stack.

# Python provides a built-in list type that can be used as a stack. Additionally, the `collections.deque` module can be used for an efficient stack implementation.

# Using list as a stack
print("--- Stack Implementation using Python List ---")
stack = []  # Initialize an empty stack

# Push operation
stack.append(10)  # Add 10
stack.append(20)  # Add 20
stack.append(30)  # Add 30
print("Stack after pushes:", stack)  # [10, 20, 30]

# Pop operation
popped_element = stack.pop()  # Remove the last element
print("Popped element:", popped_element)  # 30
print("Stack after pop:", stack)  # [10, 20]

# Peek operation (view top element without removing it)
if stack:
    print("Top element (peek):", stack[-1])  # 20

# Size of the stack
print("Size of stack:", len(stack))  # 2

# Check if stack is empty
print("Is stack empty?", len(stack) == 0)  # False

# Using collections.deque for stack
print("\n--- Stack Implementation using collections.deque ---")
from collections import deque

stack = deque()  # Initialize an empty stack

# Push operation
stack.append(40)  # Add 40
stack.append(50)  # Add 50
stack.append(60)  # Add 60
print("Stack after pushes:", list(stack))  # [40, 50, 60]

# Pop operation
popped_element = stack.pop()  # Remove the last element
print("Popped element:", popped_element)  # 60
print("Stack after pop:", list(stack))  # [40, 50]

# Peek operation (view top element without removing it)
if stack:
    print("Top element (peek):", stack[-1])  # 50

# Size of the stack
print("Size of stack:", len(stack))  # 2

# Check if stack is empty
print("Is stack empty?", len(stack) == 0)  # False

# Summary of built-in functions used:
# - list.append(x): Adds x to the end of the list (acts as push for stack).
# - list.pop(): Removes and returns the last element of the list (acts as pop for stack).
# - len(list): Returns the number of elements in the list (size of the stack).
# - list[-1]: Retrieves the last element without removing it (peek operation).
#
# The collections.deque module is preferred when frequent pop and append operations are required, as it provides O(1) time complexity for these operations, unlike the list which may incur O(n) in certain scenarios.
