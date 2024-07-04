# Question: What will the output of the following code be?

a = "hello"
b = "world"
a, b = b, a
print(a + " " + b)


# world hello


# Question 1: String Immutability
# Question: What will be the output of the following code?

s = "hello"
s[0] = "H"
print(s)  # TypeError: 'str' object does not support item assignment


# Question 2: String Multiplication
# Question: What will the output of the following code be?

print("a" * 5)
print("a" * 0)
print("a" * -1)

# aaaaa


# Question 3: String Concatenation with +=
# Question: What will be the output of the following code?

s = "hello"
s += " world"
print(s)   #  hello world

# Explanation: The += operator concatenates the right operand to the left operand and assigns the result to the left operand. This operation creates a new string and assigns it to s.

# Question 4: String Slicing
# Question: What will the output of the following code be?


s = "abcdef"
print(s[1:5])
print(s[:3])
print(s[3:])
print(s[-1])
print(s[::-1])


# bcde
# abc
# def
# f
# fedcba


# Question 5: Checking for Substring
# Question: What will the output of the following code be?

s = "hello world"
print("world" in s)
print("WORLD" in s)

# True
# False


# Question 1: str.join()
# Question: What will the output of the following code be?

s = "-"
seq = ("a", "b", "c")
print(s.join(seq))  # a-b-c


# Question 2: str.split()
# Question: What will the output of the following code be?

s = "one two three"
print(s.split())
print(s.split(" "))
print(s.split("e"))

# ['one', 'two', 'three']
# ['one', 'two', 'three']
# ['on', ' two thr', '', '']

# Question 3: str.strip()
# Question: What will the output of the following code be?

s = "  hello  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# hello
# hello  
# hello


# Question 4: str.replace()
# Question: What will the output of the following code be?

s = "hello world"
print(s.replace("l", "x"))
print(s.replace("world", "Python"))

# hexxo worxd
# hello Python

# Question 5: str.upper() and str.lower()
# Question: What will the output of the following code be?

s = "Hello World"
print(s.upper())
print(s.lower())

# HELLO WORLD
# hello world


# Question 6: str.startswith() and str.endswith()


s = "hello world"
print(s.startswith("hello"))
print(s.endswith("world"))
print(s.startswith("world"))
print(s.endswith("hello"))

# True
# True
# False
# False


# Question 7: str.find()  Explanation: The str.find() method returns the lowest index of the substring if it is found, otherwise it returns -1.



s = "hello world"
print(s.find("o"))  # 4
print(s.find("world"))  # 6
print(s.find("Python")) # -1


# Question 8: str.count()  The str.count() method returns the number of non-overlapping occurrences of a substring.

s = "banana"
print(s.count("a"))    #3
print(s.count("na"))    # 2 
print(s.count("b"))     # 1


# Question 1: str.isalnum()  --> only letters and numbers

s1 = "hello123"
s2 = "hello 123"
s3 = "hello_123"
print(s1.isalnum())  # True
print(s2.isalnum())  # False
print(s3.isalnum())  # False

# Question 2: str.isalpha()  --> The str.isalpha() method returns True if all characters in the string are alphabetic and there is at least one character, otherwise it returns False.

s1 = "hello"
s2 = "hello123"
s3 = "hello_123"
print(s1.isalpha())  # True
print(s2.isalpha())  # False
print(s3.isalpha())  # False


# Question 3: str.isdigit()  --> Explanation: The str.isdigit() method returns True if all characters in the string are digits and there is at least one character, otherwise it returns False.

s1 = "12345"
s2 = "12345a"
s3 = "123 45"
print(s1.isdigit())   # True
print(s2.isdigit())   # False
print(s3.isdigit())   # False


# str.islower() and str.isupper()

s1 = "hello"
s2 = "Hello"
s3 = "HELLO"
print(s1.islower())   # True
print(s2.islower())   # False
print(s3.islower())   # False
print(s1.isupper())   # False
print(s2.isupper())   # False
print(s3.isupper())   # True

# Question 5: str.isspace()  --> Explanation: The str.isspace() method returns True if there are only whitespace characters in the string and there is at least one character, otherwise it returns False.

s1 = "   "
s2 = "  a  "
s3 = "\t\n"
print(s1.isspace())   # True
print(s2.isspace())   # False
print(s3.isspace())   # True







