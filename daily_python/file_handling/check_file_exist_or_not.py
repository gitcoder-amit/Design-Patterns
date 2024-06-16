'''
Check file exist or not? -> 
isfile() -> this method is used  to check file exist or not 
this method belongs to path module  which is sub module of os module

syntax -->
      import os
      os.path.isfile(filename)
'''

import os
print(os.path.isfile('data.txt'))  # True
print(os.path.isfile('data1.txt'))  # False

if os.path.isfile('data.txt'):
    f = open('data.txt')
    # operation
    f.close()
else:
    print('file not exist')