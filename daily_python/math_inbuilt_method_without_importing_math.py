# to use ceil, floor we need to import math module

# Example usage of built-in math functions

numbers = [3.5, -4.2, 5, 7, -2.3]

# Absolute values
abs_values = [abs(num) for num in numbers]
print(abs_values)  # Output: [3.5, 4.2, 5, 7, 2.3]

# Maximum and Minimum
print(max(numbers))  # Output: 7
print(min(numbers))  # Output: -4.2

# Sum
print(sum(numbers))  # Output: 9.0

# Power
print(pow(2, 3))  # Output: 8

# Rounding
print(round(3.14159, 2))  # Output: 3.14


# These built-in functions provide essential mathematical operations and are sufficient for many common tasks. For more advanced mathematical operations, such as trigonometry, logarithms, or working with complex numbers, you would typically use the math module or other specialized libraries like numpy. However, for basic arithmetic and simple mathematical operations, Python's built-in functions are more than adequate.