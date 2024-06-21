'''
  whenever we open a text file, a cursor is set initialy it is present in begining --> 0 position

  tell() --> this method is used to find the current position of a file pointer from the begining of the file
             Position starts from 0. It is just like indexing in string
             file_object.tell()  # it will return current position from start

  seek() --> This method is used to change the position of file pointer
            Remember file pointer position is always counted from the beginning 
            file_object.seek(position)  # now the cursor will point at position
'''

f = open('data.txt', mode='r')
print(f.tell()) # 0
f.read(3)
print(f.tell()) #3
f.read()
print(f.tell())  #85 last of file
f.close()


f = open('data.txt', mode='r')
print(f.tell())  # 0
f.read(3)
print(f.tell())  # 3
f.seek(0)
print(f.tell()) # 0
print(f.read)   # this will print whole file due to cursor is at start
f.close()