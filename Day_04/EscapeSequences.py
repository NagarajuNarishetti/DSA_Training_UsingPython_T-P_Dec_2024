# Demonstrating Escape Sequences in Python

# 1. Newline and Horizontal Tab
print("Example 1:")
print("Hello\nWorld")  # Newline: Moves to the next line
# Output:
# Hello
# World

print("Hello\tWorld")  # Horizontal tab: Adds a tab space
# Output: Hello    World

# 2. Quotes Inside Strings
print("\nExample 2:")
print("She said, \"Python is awesome!\"")  # Double quotes
# Output: She said, "Python is awesome!"

print('It\'s a great day!')  # Single quote
# Output: It's a great day!

# 3. Backslash
print("\nExample 3:")
print("This is a backslash: \\")
# Output: This is a backslash: \

# 4. Unicode Characters
print("\nExample 4:")
print("\u2764")  # Unicode for a heart symbol
# Output: ❤
print("\N{Smiling Face}")  # Unicode by name
# Output: ☺

# 5. Bell Sound (system dependent)
print("\nExample 5:")
print("\a")  # Produces a beep sound if enabled on the system
# Output: (Beep sound if supported)

# 6. Backspace
print("\nExample 6:")
print("Hello\bWorld")  # Backspace removes the character before '\b'
# Output: HellWorld

# 7. Form Feed
print("\nExample 7:")
print("Hello\fWorld")  # Form feed (page break effect)
# Output: 
# Hello
#      World

# 8. Carriage Return
print("\nExample 8:")
print("Hello\rWorld")  # Carriage return moves to the beginning of the line
# Output: World

# 9. Vertical Tab
print("\nExample 9:")
print("Hello\vWorld")  # Vertical tab
# Output:
# Hello
#  World

# 10. Octal and Hexadecimal
print("\nExample 10:")
print("\101")  # Octal value for 'A'
# Output: A
print("\x41")  # Hexadecimal value for 'A'
# Output: A

# 11. Raw Strings
print("\nExample 11:")
print(r"C:\Users\Nagi\Documents")  # Raw string prevents escape sequences
# Output: C:\Users\Nagi\Documents

# 12. Unicode with 32-bit Hexadecimal
print("\nExample 12:")
print("\U0001F600")  # Unicode for grinning face emoji
# Output: 😀

# Practical Example: File Path and Formatting
print("\nPractical Example:")
print("Path: C:\\Users\\Nagi\\Documents")  # Using escape sequences
# Output: Path: C:\Users\Nagi\Documents

print(r"Path: C:\Users\Nagi\Documents")  # Using raw string
# Output: Path: C:\Users\Nagi\Documents

print("Name:\tNagi\nAge:\t20")  # Formatting output with tab and newline
# Output:
# Name:   Nagi
# Age:    20
