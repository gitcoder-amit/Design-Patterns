# Using the sorted() function in Python, you can sort various types of iterable objects, including lists, tuples, dictionaries, and more. Here's a breakdown of what you can do with sorted():


# Sort lists and tuples:

my_list = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_list = sorted(my_list)
print(sorted_list)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]

# Sort dictionaries by keys or values:

my_dict = {'a': 3, 'b': 1, 'c': 4}
sorted_dict_by_keys = sorted(my_dict.items())  # Sort by keys
sorted_dict_by_values = sorted(my_dict.items(), key=lambda item: item[1])  # Sort by values

# Custom sorting using a key function:

my_list = ['banana', 'apple', 'cherry']
sorted_list = sorted(my_list, key=len)  # Sort by length of strings
print(sorted_list)  # Output: ['apple', 'cherry', 'banana']

# Reverse sorting:

my_list = [3, 1, 4, 1, 5, 9, 2, 6]
reverse_sorted_list = sorted(my_list, reverse=True)
print(reverse_sorted_list)  # Output: [9, 6, 5, 4, 3, 2, 1, 1]

# Sorting mixed types:

my_list = [3, 'apple', 1, 'banana', 4, 'cherry']
sorted_list = sorted(my_list, key=str)  # Sort by string representation
print(sorted_list)  # Output: [1, 3, 4, 'apple', 'banana', 'cherry']


# Using a custom sorting algorithm:

def custom_sort(item):
    # Custom sorting logic
    return ...

my_list = [...]  # Your list of items
sorted_list = sorted(my_list, key=custom_sort)


# Sorting nested data structures:

my_list = [(2, 'apple'), (1, 'banana'), (3, 'cherry')]
sorted_list = sorted(my_list, key=lambda x: x[1])  # Sort tuples by second element



my_list = [(2, 'apple', 1), (1, 'banana', 4), (3, 'cherry', 3)]
sorted_list = sorted(my_list, key=lambda x: x[2])  # Sort tuples by third element
print(sorted_list)


my_dict = {'a': [3, 2, 4], 'b': [3,1, 1], 'c': [3,4, 2]}
sorted_dict_by_keys = sorted(my_dict.items() , key = lambda x : x[1][2])  # Sort by last value of values
print(sorted_dict_by_keys)  # [('b', [3, 1, 1]), ('c', [3, 4, 2]), ('a', [3, 2, 4])]

