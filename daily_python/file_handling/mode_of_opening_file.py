'''
Mode of opening file :-
    when we open a file  for operations, you have to specify mode. mode specifies the purpose of opening file.There are two type of modes
    1. Text modes
    2. Binary Modes

    Text Mode -> when we open a file  in text modes, python treats it's  content as str type
                when we get data  from a text mode file, python first decodes the raw bytes using either a platform dependent encoding or specified encoding
    
    r --> Open file for reading only. If  the file doesn't exist. It will show FileNotFoundError
    w --> open file for writing only. If the file doesn't exist. it will create a file
    a --> open for appending. It appends new data at end of file. If file does not exist. It creates a new file
    x --> open for exclusive creation for writing. The specified file must not be available. It creates a new file  and then  we write data into it. If file exists. It will give an error.
    r+ --> Open for reading  and then writing 
    w+ --> Open for writing and then reading
    a+ --> Open for appending  and then writing


    Binary Mode -> when we open a file in binary mode, python uses the data without any encoding. Binary mode file    reflects the raw data directly in the file
        Python treats file content  as bytes type. These modes are used  while dealing  with nontext file like images, audios, videos etc

    rb --> Open for reading in binary mode(same as text b)
    wb -->Open for writing in binary mode( same as text w)
    ab --> Open for appending (same as text a)
    xb --> Open for exclusive creation and writing same as x
    rb+ --> Open for read and then write in binary
    wb+ --> Open for writing  and then reading in binary
    ab+ --> Open for  append  and then read  in binary
'''


f = open("data.txt", mode = 'r')
print(f.read())
f.close()

f = open('data.txt', mode = 'rb')
print(f.read())
f.close()