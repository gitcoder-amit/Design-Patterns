
# T --> O(N**2)
def find_subarray(arr, target):
    n = len(arr)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum == target:
                return arr[i:j+1]
    return False


# T --> O(N)    
def find_subarray1(arr, target): 
    n = len(arr)
    sum = 0
    start_index = 0
    for i in range(n):
        sum += arr[i]
        while sum > target:
            sum -= arr[start_index]
            start_index += 1
            
        if sum == target:
            return arr[start_index:i+1]
        
    return False
            
    
arr = [1,2,5,10,3,20,7]
target = 33
print(find_subarray1(arr, 33))
                
    