# 1

a = [[]] * 3
a[0].append(1)
print(a)  # [[1], [1], [1]]

a[1].append(2)
print(a)  # [[1, 2], [1, 2], [1, 2]]

a[2] = [3]
print(a)  # [[1, 2], [1, 2], [3]]


# 2

words = ['apple', 'banana', 'cherry']

# List of lengths of each word
lengths = [len(word) for word in words]
print(lengths)  # [5, 6, 6]

# Filtered list of words with length >= 6
filtered_words = [word for word in words if len(word) >= 6]
print(filtered_words)  # ['banana', 'cherry']

# 3

import copy

# Original list
original = [1, 2, [3, 4]]

# Shallow copy
shallow_copy = copy.copy(original)
shallow_copy[2][0] = 'changed'
print(original)  # [1, 2, ['changed', 4]]
print(shallow_copy)  # [1, 2, ['changed', 4]]

# Deep copy
deep_copy = copy.deepcopy(original)
deep_copy[2][1] = 'deep_changed'
print(original)  # [1, 2, ['changed', 4]]
print(deep_copy)  # [1, 2, ['changed', 'deep_changed']]

# Explanation: A shallow copy creates a new list but does not create copies of nested objects; they remain as references. A deep copy creates a new list and recursively copies all nested objects, so modifications to the deep copy do not affect the original list.

# 4. List Indexing and Unpacking

lst = [1, 2, 3, 4, 5]

a, *b, c = lst
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5


# 5. In-Place Modification vs New List Creation

lst = [1, 2, 3, 4, 5, 6]

lst[:] = [x for x in lst if x % 2 != 0]
print(lst)  # [1, 3, 5]


# 6. List Comprehension with Condition

nums = [1, -2, 3, -4, 5, -6]

squared_positives = [x**2 for x in nums if x > 0]
print(squared_positives)  # [1, 9, 25]

# 7. Flattening a Nested List

def flatten(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        else:
            flattened.append(item)
    return flattened

lst = [[1, 2, 3], [4, 5], [6, [7, 8]]]
print(flatten(lst))  # [1, 2, 3, 4, 5, 6, 7, 8]


# 8. Combining Lists Alternately

a = [1, 3, 5]
b = [2, 4, 6]

c = [item for pair in zip(a, b) for item in pair]
print(c)  # [1, 2, 3, 4, 5, 6]

# 9. Mutable Default Arguments

def add_to_list(element, lst=[]):
    lst.append(element)
    return lst

print(add_to_list(1))  # [1]
print(add_to_list(2))  # [1, 2]
print(add_to_list(3, []))  # [3]
print(add_to_list(4))  # [1, 2, 4]

# Explanation: The default argument lst=[] is evaluated once when the function is defined, not each time the function is called. Therefore, when add_to_list is called without a second argument, it modifies the same default list. Passing an explicit list ([]) as the second argument creates a new list for that particular function call.

# 10. Passing by Reference

def modify_list(lst):
    lst.append(4)
    lst[0] = 99

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [99, 2, 3, 4]

# Explanation: Lists in Python are passed by reference. This means that any modifications made to the list within the function will affect the original list. The modify_list function appends 4 to lst and sets the first element to 99, which changes my_list directly.

# 11. Nested Lists and Mutation

def extend_list(val, lst=[]):
    lst.append(val)
    return lst

list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')

print("list1:", list1)  # list1: [10, 'a']
print("list2:", list2)  # list2: [123]
print("list3:", list3)  # list3: [10, 'a']

# Explanation: Similar to the first example, the default list lst=[] is shared between calls where no second argument is provided. list1 and list3 share the same default list, while list2 gets a fresh list.


# 4. Modifying List within a Function

def append_element(lst, element):
    lst.append(element)
    return lst

my_list = [1, 2, 3]
new_list = append_element(my_list, 4)
new_list.append(5)

print(my_list)  # [1, 2, 3, 4, 5]
print(new_list)  # [1, 2, 3, 4, 5]

# Explanation: my_list and new_list refer to the same list object in memory. Modifications to one are reflected in the other.

# 5. List Copying

def modify_list(lst):
    lst = lst + [4]  # This creates a new list object
    lst[0] = 99

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3]

# Explanation: The statement lst = lst + [4] creates a new list object and assigns it to lst within the function. This does not modify the original my_list outside the function scope. Hence, my_list remains unchanged.


# 5. List Copying

def modify_list(lst):
    lst = lst  # This will not create a new list object just referencing to same list
    lst[0] = 99

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [99, 2, 3]






