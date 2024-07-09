''' 
    when we create class in python,
    One class object is created for class --> we dont need to create automatically created when we create class
    We can create instance object as many as we want


    class object contain static member variable. we can access class object by using class name

'''

class Test:
    x = 10  # static variable

    def __init__(self, a, b):
        self.a = a
        self.b = b


print(Test.x)
# t1 = Test()  --> this is an instance object

t1 = Test(4, 5)
print(t1.a)


