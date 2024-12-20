# Arrays (Lists) in Python

# 1. Creating an Array (List)
arr = [1, 2, 3, 4, 5]
print("Original Array:", arr)  # Output: [1, 2, 3, 4, 5]

# 2. Accessing Array Elements
print("First Element:", arr[0])  # Output: 1
print("Last Element:", arr[-1])  # Output: 5

# 3. Modifying an Array
arr[2] = 10  # Changing third element (index 2) to 10
print("Array after modification:", arr)  # Output: [1, 2, 10, 4, 5]

# 4. Appending Elements to an Array
arr.append(6)  # Adds 6 to the end of the array
print("Array after appending 6:", arr)  # Output: [1, 2, 10, 4, 5, 6]

# 5. Inserting Elements at a Specific Position
arr.insert(1, 7)  # Inserts 7 at index 1
print("Array after inserting 7 at index 1:", arr)  # Output: [1, 7, 2, 10, 4, 5, 6]

# 6. Removing Elements from an Array
arr.remove(10)  # Removes first occurrence of 10
print("Array after removing 10:", arr)  # Output: [1, 7, 2, 4, 5, 6]

# 7. Popping Elements from an Array
arr.pop(2)  # Removes element at index 2
print("Array after popping index 2:", arr)  # Output: [1, 7, 4, 5, 6]

# 8. Finding the Length of an Array
print("Length of Array:", len(arr))  # Output: 5

# 9. Slicing Arrays
sliced_array = arr[1:4]  # Slicing the array from index 1 to 3 (excluding index 4)
print("Sliced Array (index 1 to 3):", sliced_array)  # Output: [7, 4, 5]

# 10. Looping Through an Array
print("Looping through Array:")
for element in arr:
    print(element)  # Output: 1 7 4 5 6

# 11. Sorting the Array
arr.sort()  # Sorts the array in ascending order
print("Array after sorting:", arr)  # Output: [1, 4, 5, 6, 7]

# 12. Reversing the Array
arr.reverse()  # Reverses the array in place
print("Array after reversing:", arr)  # Output: [7, 6, 5, 4, 1]

# --------------------------------------------
# **Array Methods:**
# - append(x): Adds x to the end of the array.
# - insert(i, x): Inserts x at position i.
# - remove(x): Removes the first occurrence of x from the array.
# - pop(i): Removes the element at position i.
# - index(x): Returns the index of the first occurrence of x.
# - count(x): Returns the number of occurrences of x in the array.
# - sort(): Sorts the array in place.
# - reverse(): Reverses the array in place.

# Example Output:

# Original Array: [1, 2, 3, 4, 5]
# First Element: 1
# Last Element: 5
# Array after modification: [1, 2, 10, 4, 5]
# Array after appending 6: [1, 2, 10, 4, 5, 6]
# Array after inserting 7 at index 1: [1, 7, 2, 10, 4, 5, 6]
# Array after removing 10: [1, 7, 2, 4, 5, 6]
# Array after popping index 2: [1, 7, 4, 5, 6]
# Length of Array: 5
# Sliced Array (index 1 to 3): [7, 4, 5]
# Looping through Array:
# 1
# 7
# 4
# 5
# 6
# Array after sorting: [1, 4, 5, 6, 7]
# Array after reversing: [7, 6, 5, 4, 1]

# --------------------------------------------

# **Key Points about Lists in Python (Arrays):**
# 1. **Creating**: Lists are created using square brackets []. You can store any type of element in a list (numbers, strings, other lists).
# 2. **Accessing Elements**: You can access elements by their index. Python uses 0-based indexing, meaning the first element has index 0.
# 3. **Modifying Elements**: You can modify any element by directly assigning a new value using the index.
# 4. **Appending/Removing Elements**: Use append() to add elements at the end or remove() to delete a specific value. pop() removes an element by index.
# 5. **Length**: The len() function returns the number of elements in a list.
# 6. **Slicing**: Lists can be sliced to extract sub-lists. You can use slicing with start, stop, and step indices.
# 7. **Iteration**: You can use a for loop to iterate through a list and perform operations on each element.
# 8. **Sorting and Reversing**: Use sort() to sort the list in place and reverse() to reverse the order.

# --------------------------------------------
# **Conclusion:**
# This is a comprehensive guide to working with arrays (lists) in Python. It covers how to create, modify, access, and manipulate lists, along with examples of common list operations. You can use this as a reference for all basic list operations in Python.
