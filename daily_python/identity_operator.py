'''
identity operator --> is used to check two refernce varialbe are refering to same object or not
is 
is not

is checks for value as well as memory location
== checks only for value
'''

x = 5
y = 5  # in this no new object created just one reference increassed

print(x is y)


a = [1, 2, 3]
b = [1, 2, 3]
g = a

dic1 = {'name':'amit'}
dic2 = {'name' : 'amit'}

c = 4
d = 4

e = "abc"
f = "abc"

print(a is b)
print( c is d)
print( e is f)

print(dic1 is dic2)
print( g is a)

# False
# True
# True
# False
# True