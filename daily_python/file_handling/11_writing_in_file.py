'''
 In order to write data in file, we have to  open in a mode which provides  the facility of writing data ex -> w, a, x etc

 w mode --> It opens the file to write only
            It overrites the data in a file 
            If a file doesn't exist, it creates  a new file and write into it
            the file pointer exists at the begining of file 

            mainly two methods are used for writing data in a file
            write()  --> file_object.write(data in string format)
            writelines()  --> this method is used to write a group of lines of strings into the file represented by a file object
                              Group of strings are stored in list, tuple or set
                              file_object.writelines(list/set/tuple)


'''


f = open('data1.txt', mode='w')
f.write("My name is \namit yadav")  # we can break the line using \n  write in start in file due to cursor at 0
n = f.write("bye bye")   # this will write next to amit yadav also returns no of characters it is writing in file
print(n)
f.close()

f = open('data1.txt', mode='w')
lines_list = ['yogesh\n', 'ram\n', 'raj', 'amit']
f.writelines(lines_list)
f.close()