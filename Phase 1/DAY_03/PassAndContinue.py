# Example 1: Using `pass` in a loop as a placeholder
# ----------------------------------------------------
print("Example 1: Demonstrating 'pass'")
for i in range(5):
    if i == 2:
        pass  # Placeholder: No action taken for i == 2
        print(f"Encountered pass at i={i}, doing nothing.")
    print(f"Current value of i: {i}")

# Output:
# Current value of i: 0
# Current value of i: 1
# Encountered pass at i=2, doing nothing.
# Current value of i: 2
# Current value of i: 3
# Current value of i: 4


# Example 2: Using `continue` to skip certain iterations
# ------------------------------------------------------
print("\nExample 2: Demonstrating 'continue'")
for i in range(5):
    if i == 2:
        print(f"Skipping iteration at i={i} using continue.")
        continue  # Skip the rest of the loop body when i == 2
    print(f"Current value of i: {i}")

# Output:
# Current value of i: 0
# Current value of i: 1
# Skipping iteration at i=2 using continue.
# Current value of i: 3
# Current value of i: 4


# Example 3: `pass` in an empty function
# --------------------------------------
print("\nExample 3: Using 'pass' in a function")
def placeholder_function():
    pass  # Function not implemented yet, avoids syntax error

placeholder_function()
print("Placeholder function executed without doing anything.")

# Output:
# Placeholder function executed without doing anything.


# Example 4: `continue` in a loop to skip even numbers
# ----------------------------------------------------
print("\nExample 4: Skipping even numbers using 'continue'")
for i in range(5):
    if i % 2 == 0:  # If i is even
        print(f"Skipping even number: {i}")
        continue
    print(f"Odd number: {i}")

# Output:
# Skipping even number: 0
# Odd number: 1
# Skipping even number: 2
# Odd number: 3
# Skipping even number: 4


# Example 5: Using `pass` in a conditional statement
# --------------------------------------------------
print("\nExample 5: Demonstrating 'pass' in a conditional")
x = 10
if x > 5:
    pass  # Placeholder for future code
    print("x is greater than 5, but no specific action is taken.")

# Output:
# x is greater than 5, but no specific action is taken.


# Example 6: Combining `pass` and `continue` in a loop
# -----------------------------------------------------
print("\nExample 6: Combining 'pass' and 'continue'")
for i in range(5):
    if i == 2:
        pass  # Placeholder: No action taken for i == 2
        print(f"'pass' executed at i={i}.")
    if i == 3:
        print(f"Skipping iteration at i={i} using 'continue'.")
        continue
    print(f"Processing i: {i}")

# Output:
# Processing i: 0
# Processing i: 1
# 'pass' executed at i=2.
# Processing i: 2
# Skipping iteration at i=3 using 'continue'.
# Processing i: 4
