# heapq is a module in Python's standard library that provides an implementation of the heap queue algorithm, also known as the priority queue algorithm. Heaps are binary trees for which every parent node has a value less than or equal to any of its children. This makes them suitable for implementing priority queues where the smallest element is always at the root.

# Key Features of heapq:
# Min-Heap by Default: The heapq module in Python implements a min-heap, meaning the smallest element is always the root of the heap.
# Efficient Operations: Insertion, deletion, and retrieval of the smallest element all have an average time complexity of 
# 𝑂
# (
# log
# ⁡
# 𝑛
# )
# O(logn).
# Basic Operations:
# Creating a Heap:

# Any list can be turned into a heap using heapq.heapify(). This function rearranges the elements to satisfy the heap property.
# Pushing Elements:

# Use heapq.heappush(heap, item) to add a new item to the heap, maintaining the heap property.
# Popping Elements:

# Use heapq.heappop(heap) to remove and return the smallest item from the heap.
# Peek at the Smallest Element:

# The smallest item is always at heap[0] without removing it from the heap.
# Push and Pop:

# heapq.heappushpop(heap, item) pushes the new item onto the heap and then pops the smallest item off.
# Pop and Push:

# heapq.heapreplace(heap, item) pops the smallest item and then pushes the new item onto the heap. This operation is more efficient than performing a heappop() followed by heappush().
# Finding N Largest or Smallest Elements:

# heapq.nlargest(n, iterable) returns the n largest elements from the dataset.
# heapq.nsmallest(n, iterable) returns the n smallest elements.
# Examples:
Let's look at some practical examples using the heapq module.

python
Copy code
import heapq

# Example list
nums = [4, 1, 7, 3, 8, 5]

# Convert list into a heap
heapq.heapify(nums)
print("Heapified list:", nums)
# Output: Heapified list: [1, 3, 5, 4, 8, 7]

# Push a new element onto the heap
heapq.heappush(nums, 2)
print("After pushing 2:", nums)
# Output: After pushing 2: [1, 3, 2, 4, 8, 7, 5]

# Pop the smallest element from the heap
smallest = heapq.heappop(nums)
print("Popped smallest element:", smallest)
print("Heap after popping:", nums)
# Output: Popped smallest element: 1
#         Heap after popping: [2, 3, 5, 4, 8, 7]

# Peek at the smallest element without popping it
print("Smallest element:", nums[0])
# Output: Smallest element: 2

# Push and pop an element in one operation
result = heapq.heappushpop(nums, 6)
print("Result of pushpop operation:", result)
print("Heap after pushpop:", nums)
# Output: Result of pushpop operation: 2
#         Heap after pushpop: [3, 4, 5, 6, 8, 7]

# Pop and push an element in one operation
result = heapq.heapreplace(nums, 1)
print("Result of heapreplace operation:", result)
print("Heap after heapreplace:", nums)
# Output: Result of heapreplace operation: 3
#         Heap after heapreplace: [1, 4, 5, 6, 8, 7]

# Get the 3 largest elements from the heap
largest_three = heapq.nlargest(3, nums)
print("3 largest elements:", largest_three)
# Output: 3 largest elements: [8, 7, 6]

# Get the 3 smallest elements from the heap
smallest_three = heapq.nsmallest(3, nums)
print("3 smallest elements:", smallest_three)
# Output: 3 smallest elements: [1, 4, 5]
Use Cases:
Priority Queues:

heapq is commonly used to implement priority queues where the task with the highest priority (usually the smallest value in a min-heap) is processed first.
Scheduling:

Tasks with deadlines or priorities can be efficiently managed using heaps.
Graph Algorithms:

Heaps are crucial in algorithms like Dijkstra's shortest path or Prim's minimum spanning tree, where they help efficiently retrieve the next minimum edge or shortest path.
Stream Processing:

Finding the n smallest or largest elements in a stream of data can be efficiently handled using heapq.
Advanced Usage:
Using Custom Objects: You can use heaps with custom objects by defining a comparison method (__lt__) in your class to determine the order.
Max-Heap: Python’s heapq is a min-heap by default. To simulate a max-heap, you can invert the values (e.g., by storing the negative of the values).
Custom Object Example:
If you want to use heapq with custom objects, you can define the comparison operators in your class.

python
Copy code
import heapq

class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __repr__(self):
        return f"Task(priority={self.priority}, description='{self.description}')"

# Example usage
tasks = [
    Task(3, 'Write code'),
    Task(1, 'Do homework'),
    Task(2, 'Read book')
]

heapq.heapify(tasks)
print("Heapified tasks:", tasks)

# Push a new task
heapq.heappush(tasks, Task(0, 'Urgent Task'))
print("After pushing new task:", tasks)

# Pop the highest priority task (lowest number)
highest_priority_task = heapq.heappop(tasks)
print("Popped task:", highest_priority_task)
print("Heap after popping:", tasks)
In this example, tasks are prioritized by their priority attribute. The __lt__ method defines that a task with a lower priority number has higher priority in the heap.

Conclusion:
The heapq module is a powerful tool for efficiently managing collections of data where the smallest (or largest) element needs to be frequently accessed or manipulated. It’s widely used in scenarios requiring efficient priority queue implementations and supports both basic and advanced use cases.





