# Initialize a dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}

# 1. clear() - Removes all elements
dict1.clear()
print(dict1)  # Output: {}

# Reinitialize dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}

# 2. copy() - Creates a shallow copy of the dictionary
dict_copy = dict1.copy()
print(dict_copy)  # Output: {'a': 1, 'b': 2, 'c': 3}

# 3. fromkeys() - Creates a dictionary with specified keys and a single value
keys = ['x', 'y', 'z']
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'x': 0, 'y': 0, 'z': 0}

# 4. get() - Gets the value for a key, with an optional default
print(dict1.get('b'))  # Output: 2
print(dict1.get('z', 'Not Found'))  # Output: Not Found

# 5. items() - Returns key-value pairs
print(dict1.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# 6. keys() - Returns all the keys
print(dict1.keys())  # Output: dict_keys(['a', 'b', 'c'])

# 7. pop() - Removes a key and returns its value
print(dict1.pop('b'))  # Output: 2
print(dict1)  # Output: {'a': 1, 'c': 3}

# 8. popitem() - Removes and returns the last key-value pair
print(dict1.popitem())  # Output: ('c', 3)
print(dict1)  # Output: {'a': 1}

# Reinitialize dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}

# 9. setdefault() - Adds a key with a default value if it doesn't exist
print(dict1.setdefault('d', 4))  # Output: 4
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 10. update() - Updates the dictionary with another dictionary or key-value pairs
dict1.update({'e': 5, 'f': 6})
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# 11. values() - Returns all the values
print(dict1.values())  # Output: dict_values([1, 2, 3, 4, 5, 6])

# 12. Membership operators (in, not in) - Check if a key exists
print('a' in dict1)  # Output: True
print('z' not in dict1)  # Output: True

# 13. Deleting a key
del dict1['a']
print(dict1)  # Output: {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# 14. Iterating over a dictionary
for key, value in dict1.items():
    print(f"{key}: {value}")
# Output:
# b: 2
# c: 3
# d: 4
# e: 5
# f: 6

# 15. Using dict comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 16. Using the `len()` function - Get the number of keys
print(len(dict1))  # Output: 5

# 17. Using `max()` and `min()` with keys
print(max(dict1))  # Output: f (based on lexicographical order)
print(min(dict1))  # Output: b (based on lexicographical order)

# 18. Nested dictionaries
nested_dict = {'person1': {'name': 'Alice', 'age': 25},
               'person2': {'name': 'Bob', 'age': 30}}
print(nested_dict['person1']['name'])  # Output: Alice

# 19. Sorting a dictionary by keys
sorted_dict = dict(sorted(dict1.items()))
print(sorted_dict)  # Output: {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# 20. Dictionary with default values using `collections.defaultdict`
from collections import defaultdict
default_dict = defaultdict(int)  # Default value for missing keys is 0
default_dict['x'] += 1
print(default_dict)  # Output: defaultdict(<class 'int'>, {'x': 1})
