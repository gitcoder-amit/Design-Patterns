'''
How can we create static member varialbe?
# static variable get memory inside class object
'''


class Item:
    a = 5  # static member varialbe first way

    def __init__(self):
        self.x = 10 # instance member varialbe
        y = 4 # local variableset1.union(set2)  # {1, 2, 3, 4, 5}
# intersection(*others): 
        print(y)
        Item.b = 6 # static member variable second way

    def f1(self):
        Item.c = 7 # third way to create static member variable

    @staticmethod
    def f2():
        Item.d = 5 # 4th way to create static member varialbe

    
    @classmethod
    def f3(cls):
        cls.e = 9 # static variable 5th way
        Item.f = 10 # static varialbe 6th way


Item.g = 7 # static variable 7th way  