# syntax  f = open(filename, mode='r', buffering, encoding = None, erros = None, newline = None, closefd = None)
# buffering --> Positive integer value used to set buffer size for file
            # in text mode, buffer size  should be  1 or more than 1    
            # in binary mode buffer size can be zero 
            # default size:- 4096-8192 bytes

# suppose much data like 1 gb present in a file then we will divide the data in chunks. and each time 1 chunk will be fetched in buffer and process in python program


# Encoding --> 1. encoding type is used to decode and encode file 
            #    2. Shold be used in text mode only
            #    3. Default value depend on OS
            #    4. for window: cp1252

# error s--> Represents how encoding and decoding  errors are to be handled.
        # 2. Can't be used in Binary mode only used in text mode    
        # 3. some standard values  are:- strict, ignore, replace etc by default strict is set

# newline -> it can be \n, \r, \r\n default is \n

f = open("data.txt", mode='r')  # here we need to give full path to file otherwise file should be present in same directory
if f:
    print("file successfully opened")


print(type(f))  #<class '_io.TextIOWrapper'>

f = open('data.txt', mode='r', buffering=10, encoding='utf-8')  # I want to fetch 10 byte of file in the buffer memory in one time
if f:
    print("open")
print(f)   # <_io.TextIOWrapper name='data.txt' mode='r' encoding='utf-8'>


