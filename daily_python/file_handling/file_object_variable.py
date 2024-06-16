'''
    File Object Variables --> 
    name -> has name of specified file
    mode -> mode of specified file
    closed -> has boolean value. Shows file closed or not
    encoding -> has encoding name

    Sytax --> file_object.variable_name
'''

f = open('data.txt', 'r')
print(f.name)   # data.txt
print(f.mode)   # r
print(f.closed) # False
print(f.encoding) # UTF-8
f.close()