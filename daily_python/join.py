

# The string join() method returns a string by joining all the elements of an iterable (list, string, tuple, set), separated by the given separator.

text = ['Python', 'is', 'a', 'fun', 'programming', 'language']

# join elements of text with space
print(' '.join(text))

# Output: Python is a fun programming language

# Syntax --> string.join(iterable)
# The join() method takes an iterable (objects capable of returning its members one at a time) as its parameter.

#The join() method returns a string created by joining the elements of an iterable by the given string separator.

# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))

s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2))

# each element of s1 is separated by s2
# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1))

# 1, 2, 3, 4
# 1, 2, 3, 4
# s1.join(s2): 1abc2abc3
# s2.join(s1): a123b123c

