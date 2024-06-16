'''
Closing a file --> 
   1. After performing operations, we have to close a file.
   2. file_handler.close() --> used to close a file 

   what happens when we close a file? --> File object is deleted from memory and file is no more accessible unless we open it again

   what happens when we do not close a file? -> After program execution, python garbage collector will destroy file object  and closes file automatically --> Don't rely on garbage collector. --> Possible outcomes -> 1. Data will interrupt, 2. Memory wastage
'''


f = open('data.txt', 'r')
# operations
print(f.read)
f.close()