# Literals which u present in single ' ' or  " " will be treated as strings 
# str.captalize() converts 1st charector to upper case 
# str.upper() function will convert whole string to upper case
# len(str) length of fucntion 
Str= "sr university"

# Input string
string = "  Hello, Python World! 123   "

# 1. Basic string information
print("Original String:", string)  
# Output:   Hello, Python World! 123   
print("Length:", len(string))  
# Output: 29

# 2. String transformation functions
print("Lowercase:", string.lower())  
# Output: hello, python world! 123   
print("Uppercase:", string.upper())  
# Output: HELLO, PYTHON WORLD! 123   
print("Title Case:", string.title())  
# Output: Hello, Python World! 123   
print("Capitalize:", string.capitalize())  
# Output: hello, python world! 123   
print("Swap Case:", string.swapcase())  
# Output: hELLO, pYTHON wORLD! 123   
print("Strip:", string.strip())  
# Output: Hello, Python World! 123
print("Left Strip:", string.lstrip())  
# Output: Hello, Python World! 123   
print("Right Strip:", string.rstrip())  
# Output:   Hello, Python World! 123

# 3. Checking string properties
print("Is Alphanumeric:", string.isalnum())  
# Output: False
print("Is Alpha:", string.isalpha())  
# Output: False
print("Is Digit:", string.isdigit())  
# Output: False
print("Is Lowercase:", string.islower())  
# Output: False
print("Is Uppercase:", string.isupper())  
# Output: False
print("Is Space:", string.isspace())  
# Output: False
print("Starts With 'Hello':", string.startswith("Hello"))  
# Output: False
print("Ends With '123':", string.strip().endswith("123"))  
# Output: True

# 4. Search and replace
print("Find 'Python':", string.find("Python"))  
# Output: 8
print("Index of 'World':", string.index("World"))  
# Output: 15
print("Count of 'o':", string.count("o"))  
# Output: 3
print("Replace 'World' with 'Universe':", string.replace("World", "Universe"))  
# Output:   Hello, Python Universe! 123   

# 5. Splitting and joining
print("Split by spaces:", string.split())  
# Output: ['Hello,', 'Python', 'World!', '123']
print("Split by comma:", string.split(","))  
# Output: ['  Hello', ' Python World! 123   ']
print("Join with '-':", "-".join(['Hello', 'Python', 'World']))  
# Output: Hello-Python-World

# 6. String alignment
print("Center Align:", string.center(40, "*"))  
# Output: ****  Hello, Python World! 123   ****
print("Left Align:", string.ljust(40, "-"))  
# Output:   Hello, Python World! 123   --------
print("Right Align:", string.rjust(40, "-"))  
# Output: --------  Hello, Python World! 123   

# 7. Encoding and decoding
encoded = string.encode("utf-8")  # Encode the string
print("Encoded String:", encoded)  
# Output: b'  Hello, Python World! 123   '
decoded = encoded.decode("utf-8")  # Decode the string
print("Decoded String:", decoded)  
# Output:   Hello, Python World! 123   

# 8. Checking substring membership
print("Contains 'Python':", "Python" in string)  
# Output: True
print("Does not contain 'Java':", "Java" not in string)  
# Output: True

# 9. Formatting
formatted = "Hello, {}. Welcome to {}!".format("User", "Python")  # Using format()
print("Formatted String:", formatted)  
# Output: Hello, User. Welcome to Python!
f_string = f"Hello, {'User'}. Welcome to {'Python'}!"  # Using f-string
print("F-String:", f_string)  
# Output: Hello, User. Welcome to Python!

# 10. Z-fill (padding with zeros)
print("Z-Fill Example:", "123".zfill(5))  
# Output: 00123
