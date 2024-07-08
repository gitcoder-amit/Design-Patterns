'''
    It is a dyanamic replacement of attribute at runtime, Inside class we have varialbles, methods are there, they are known as attributes

    When we change attribute dynamically, this is called monkey patching

    Dynamically replacement is the common character of dynamic languages
'''

class Test:
    def __init__(self, x):
        self.x = x

    def get_data(self):
        print("Some code to fetch data from database")  # original data

    def f1(self): # function for some operation of data of database
        self.get_data()

    def f2(self):  # function for some operation of data of database
        self.get_data()


t1 = Test(5)
# t1.f1()
# t1.f2()
# suppose we want to check these functionlieties on test data
def new_get_data(self):
    print("some code to fetch data from test data")


Test.get_data = new_get_data
print("after monkey patching")
t1.f1()
t1.f2()