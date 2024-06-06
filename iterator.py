class NumberIterator:
    def __init__(self):
        self.numbers = [1, 2, 3]
        self.index = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index < len(self.numbers):
            n = self.numbers[self.index]
            self.index += 2
            return n
        else:
            raise StopIteration
            
    
obj = NumberIterator()
i = iter(obj)  # obj.__iter__()
print(i.__next__())
print(i.__next__())
# print(next(i))


class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i)) # prints 1
print(next(i)) # prints 2
print(next(i)) # prints 4
print(next(i)) # prints 8
print(next(i)) # raises StopIteration exception
