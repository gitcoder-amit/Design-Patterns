'''
    File Object methods --> readable(), writable()

    readable() --> this method is used to check whether file is  readable or not . True -> if readable, False -> if file is not readable

    writable() --> this method is used to check whether file is  writable or not . True -> if writable, False -> if file is not writable
'''

f = open('data.txt', mode='r')
print(f.readable())  # True
print(f.writable())  # False
f.close()