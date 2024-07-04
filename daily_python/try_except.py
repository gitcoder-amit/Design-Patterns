# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
  print(x)
except NameError:
  print("Variable x is not defined")   # output due to Nameerror
except:
  print("Something else went wrong")  


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")  # output due to no error in try


# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.


# Raise an exceptionx = -1
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")  # output


x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed"
