# In Python, a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.

# Decorator is a function that takes another function as argument, modifies that function and returns a new function that is modified


def decor_result(result_func):
    def distinction(marks): 
        for m in marks:
            if m >= 75:
                print("Distinction")
        result_func(marks)
        
    return distinction


@decor_result   # if we want to calculate distinction then include this line otherwise not include
def result(marks):
    for m in marks:
        if m >= 33:
            pass
        else:
            print("FAIL")
            break
    else:                           # this will execute in for completes its normal life
        print("PASS")


marks = [50, 40, 50, 89]
result(marks)


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
