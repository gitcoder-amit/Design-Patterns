'''
r+ --> read and write mode 
        the file pointer position at the begining of the file
        the r+ throws an error if file does not exist
        Opens an existing file without truncating it

        Use --> If we want to read data  first and write (append) data to same file

w+ mode -> Write and read mode 
           the file pointer position at the begining of the file 
           the w+ creates a new file if file does not exist
           Opens an existing file and truncate it first

           Use --> when we  want to write data and read the same data after writing 
'''

f =  open('data.txt', mode='r+')
data = f.read()
f.write("bye bye")   # if we will write first then it will just these character from start after then all same
f.close()


f = open('data.txt', mode='w+')  # it can loss the data hence w+ 
f.write("by bye")
f.seek(0)
data = f.read()
print(data)
f.close()
