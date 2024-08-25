def get_string(digit):
    if digit == 2:
        return 'abc'
    elif digit == 3:
        return 'def'
    elif digit == 4:
        return 'ghi'
    elif digit == 5:
        return 'jkl'
    elif digit == 6:
        return 'mno'
    elif digit == 7:
        return 'pqrs'
    elif digit == 8:
        return 'tuv'
    elif digit == 9:
        return 'wxyz'
    return ''

def keypad(n):
    if n == 0:
        output = []
        output.append('')
        return output

    small_number = n//10
    last_digit = n%10

    small_output = keypad(small_number)
    option_for_last_digit = get_string(last_digit)
    output = []
    for i in small_output:
        for j in option_for_last_digit:
            output.append(i+j)
    return output

print(keypad(234))




