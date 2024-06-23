'''
x mode ->
            Used to write data in file
            Note -> It writes only in a new file , if a file already present it will give error like file already exists error
'''


# f = open("data.txt", mode = 'x')
# data = "abc"
# f.write(data)  # FileExistsError:
# f.close()

f = open("one.txt", mode='x')
data = "xyz"
f.write(data)
f.close()