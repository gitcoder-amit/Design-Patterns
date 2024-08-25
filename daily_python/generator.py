'''
  Generator is a function but little special due to it is based on maths concept which name is generator
  generator generators data based on some logical pattern or series of data
  series of even numbers, ap, gp, odd numbers, prime numbers

  Generators are functions that return an iterator (a generator object) by using yield instead of return.
    They allow you to iterate over a sequence of items one at a time, rather than computing and returning all values at once.
    Generators are memory efficient because they generate values on the fly and do not store them in memory.
    They are particularly useful for generating large sequences of values or processing large files without loading everything into memory.
'''

# generator function always return iterator

# Produce n natural even numbers


def keypad_combination(n):
    if n == 0:
        output = ['']
        return output

    small_number = n//10
    last_digit = n % 10

    smalloutput = keypad_combination(small_number)

    opitoiF = get_option(last_dongo)
    output = []
    for i in smal_out:
        for j iin out:
            output.append(i+j)
    return output

# this function will return that number that we are writing next to yield but return is also used for return but the differnce is when we return value using return then with returning value control also ends and function ends but when we use yield with this value will be returns but function not ends , function just paused means this function will again execute from this point


def even_numbers(n):   
    i = 1
    while n:
        yield 2*i
        i += 1
        n -= 1

it = even_numbers(10)   # iterator which points to produced no from this generator
even_list = []

while True:
    try:
        even_list.append(next(it))
    except StopIteration:
        break

print(even_list)


