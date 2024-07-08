'''
Q --> Is python an interpreted language?
Yes --> An interpreter language is any programming language which is not in machine level code before runtime

Compiled Languages --> these languages are the languages in which source code is converted into machine code, machine code is stored in some file, when program need to run these machine code files will be executed, we can run that any no of times these files will run.

Interpreted Language -> In this no machine level code is stored to run. The source code converted into machine code by interpreter on the spot whenever we need to run the program.


In terms of Python-> when we make a program in python, we save as .py file, this file contains python code which is known as source code, this source code needs compiler

Python source code is first compiled into a binary code which is not operating system understandable code.

compiler compiles that source code and prepare byte code need to remember this is not machine code. we tell this compiler but it is little different from compiler

what is compiler --> Compiler converts source code to machine code

python source code -> compiler --> binary code

now we can distribute this binary code as a software to windows, linux, mac but this code is not understandable so not able to run this code due to no operating system can understand this byte code. If we want to make this code understand by these Operating system, for that it is necesarry to install one more software in these OS that is known as Python Virtual Machine, This PVM contains interpretere which we said interpreter of python so technically this is not an interpreter just it is a just intime compiler. There are multiple things in PVM that requires to run this byte code. This PVM is different for all OS, PVM translates this Byte code into machine code so that OS can understand run this code.

Just in time compiler basically reads line one by one in byte code and translate into machine code and provides one by one to OS so that OS can execute when OS is executing one line at that time just in time compiler reads another line convert into machine code and store these line to provide when OS free from previous line and provide to OS and so on
'''