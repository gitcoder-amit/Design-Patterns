'''
    Reading data from file --> To read content of file, we have 3 methods
        read()
        readline()
        readlines()

        read() -> this method is used to read data/content from a file and returns it as a string in text mode. It returns bytes in binary mode --> file_object.read(size) --> size is optional

        size -> it represents  the number of characters  to be read  in text mode. No need to give size in Binary mode

        readline() --> this function is used to read a single line from a file
        syntax -> file_object.readline(size)
        size -> number of characters to read from line

        readlines() -> this method is used to read all lines from a file and returns  a list of lines
'''

f = open('data.txt', mode = 'r')
data = f.read(6)  # read 6 character from start
print(data)
data1 = f.read(2)  # next 2 character
print(data1)
f.close()


f = open("data.txt", mode='r')
data = f.readline() # to read first line 
# data = f.readline(3) # to read first 3 character of line if we will check data 1 after then that will print whole first line except these 3 characters due to cursor is in first line after 3 character
data1 = f.readline()  # second line due to pointer is now at second line
print(data, end='')  # here is one \n for print and one \n for readline so we will get space after one line to remove this we need to use end = ' '
print(data1)
f.close()


f = open('data.txt', mode='r')
data = f.readlines()
print(data)  # ['Amit is graduated from Nit Srinagar,\n', 'Which is situated in Srinagar, Jammu and Kashmir']
for line in data:
    print(line, end="")
f.close()


f = open('data.txt', mode='r')
# data = f.read()
# print(list(f))  # list of all the line present in files ['Amit is graduated from Nit Srinagar,\n', 'Which is situated in Srinagar, Jammu and Kashmir']
for line in f:
    print(line) # it will print all the lines one by one of the file
f.close()