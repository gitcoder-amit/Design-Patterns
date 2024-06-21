'''Python's set data type is an unordered collection of unique and immutable elements. Sets are useful for membership testing, eliminating duplicate entries, and performing mathematical operations like union, intersection, difference, and symmetric difference. Below are some common methods associated with the set data type in Python:
'''
# Creation of a Set
# python
# Copy code
# Using curly braces
my_set = {1, 2, 3, 4}

# Using the set() function
my_set = set([1, 2, 3, 4])
# Adding and Removing Elements
# add(elem): Adds an element to the set.

my_set.add(5)
# remove(elem): Removes the specified element. Raises a KeyError if the element is not present.

my_set.remove(2)
# discard(elem): Removes the specified element if it is present. Does not raise an error if the element is not present.

my_set.discard(2)
# pop(): Removes and returns an arbitrary set element. Raises a KeyError if the set is empty.


elem = my_set.pop()
# clear(): Removes all elements from the set.

my_set.clear()
# Set Operations
# union(*others): Returns the union of the set and other sets.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)  # {1, 2, 3, 4, 5}
# intersection(*others): Returns the intersection of the set and other sets.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.intersection(set2)  # {2, 3}
difference(*others): Returns the difference of the set and other sets.

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.difference(set2)  # {1}
symmetric_difference(other): Returns the symmetric difference of the set and another set.


set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.symmetric_difference(set2)  # {1, 4}
Subset and Superset
issubset(other): Returns True if the set is a subset of another set.


set1 = {1, 2}
set2 = {1, 2, 3}
is_subset = set1.issubset(set2)  # True
issuperset(other): Returns True if the set is a superset of another set.


set1 = {1, 2, 3}
set2 = {1, 2}
is_superset = set1.issuperset(set2)  # True
isdisjoint(other): Returns True if the set has no elements in common with another set.

set1 = {1, 2}
set2 = {3, 4}
disjoint = set1.isdisjoint(set2)  # True
Copying a Set
copy(): Returns a shallow copy of the set.

set1 = {1, 2, 3}
set2 = set1.copy()
Length of a Set
len(): Returns the number of elements in the set.

set_length = len(my_set)
Membership Testing
in: Tests if an element is in the set.

exists = 3 in my_set  # True or False
These methods provide a comprehensive toolkit for managing sets and performing common set operations in Python.