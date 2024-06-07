# In Python, a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)


# I am going to divide 2 and 5
# 0.4
# I am going to divide 2 and 0
# Whoops! cannot divide


def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

printer("Hello")  # printer = star(percent(printer))("hellow")

'''
%%%%%%%%%%%%%%%
***************
Hello
***************
%%%%%%%%%%%%%%%'''
