# variable scope --> where a varialbe is visible and accesible
# score resolution --> (LEGB) -> Local ->  Enclosed -> Global -> Built in


def func1():
    a = 1
    print(a)


def func2():
    b = 2   # local variable
    print(b)


func1()
func2()