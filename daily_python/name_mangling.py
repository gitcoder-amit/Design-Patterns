'''
    Those varialbes which inside class starts with double underscore. they are special varialbe these variable names Python automatically changes internally by prefexing underscore classname  --> _Item__h
    this concepts is called name mangling
'''

class Item:
    x = 10   # static variable
    __h = 20

print(Item.x)
# print(Item.__h) # AttributeError: type object 'Item' has no attribute '__h'
print(Item._Item__h)