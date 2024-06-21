'''
In Python, *args and **kwargs are used to pass a variable number of arguments to a function. Here's a breakdown of each and how they are used:

*args
*args allows a function to accept any number of positional arguments.
The arguments are passed as a tuple.
**kwargs
**kwargs allows a function to accept any number of keyword arguments.
The arguments are passed as a dictionary.
Here's an example to illustrate both:'''

def example_function(*args, **kwargs):
    # Print positional arguments
    print("Positional arguments (*args):", args)
    
    # Print keyword arguments
    print("Keyword arguments (**kwargs):", kwargs)

# Calling the function with various positional and keyword arguments
example_function(1, 2, 3, a=4, b=5, c=6)
# In this example:

# *args will capture 1, 2, 3 as a tuple (1, 2, 3).
# **kwargs will capture a=4, b=5, c=6 as a dictionary {'a': 4, 'b': 5, 'c': 6}.
# Output of the example
# When you run the above code, the output will be:

# Positional arguments (*args): (1, 2, 3)
# Keyword arguments (**kwargs): {'a': 4, 'b': 5, 'c': 6}

# Another Example: Function to Sum Numbers and Print Additional Information

def sum_numbers(*args, **kwargs):
    total = sum(args)
    print(f"Sum of numbers: {total}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function
sum_numbers(1, 2, 3, 4, 5, name="Alice", age=30)
# Output of this example
# When you run the code, the output will be:

# Sum of numbers: 15
# name: Alice
# age: 30
# Explanation
# The sum_numbers function calculates the sum of all positional arguments.
# It then prints each key-value pair from the keyword arguments.
# Practical Usage
# Example: Logging Function

def log_message(message, *args, **kwargs):
    print(f"Message: {message}")
    if args:
        print("Details:")
        for arg in args:
            print(f" - {arg}")
    if kwargs:
        print("Additional Info:")
        for key, value in kwargs.items():
            print(f"   {key}: {value}")

# Calling the logging function
log_message("An error occurred", "File not found", "User not logged in", code=404, user="admin")
# Output

# Message: An error occurred
# Details:
#  - File not found
#  - User not logged in
# Additional Info:
#    code: 404
#    user: admin
# This function demonstrates how *args and **kwargs can be used to create flexible and extensible functions.





