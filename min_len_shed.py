import sys

def foo(positions, k):
    positions.sort()
    min_length = sys.maxsize
    n = len(positions)
    for i in range(n-k+1):
        length = positions[i+k-1] - positions[i]
        min_length = min(min_length, length)
    return min_length