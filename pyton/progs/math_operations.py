import sys
def choose_operation():
    all = '+-*/'
    the_type = input(f'{all}:')
    if the_type == '+':
        get_sum()
    elif the_type == '-':
        get_diff()
        choose_operation()
    elif the_type == '*':
        get_mult()
        choose_operation()
    elif the_type == '/':
        get_divi()
        choose_operation()
    else:
        if the_type != 'exit':
            choose_operation()
        else:
            sys.exit()
def get_sum():
    try:
        a = float(input('first >>> '))
        b = float(input('second >>> '))
        print(f'the answer is: {suma(a,b)}')
        choose_operation()
    except:
        print('invalid syntax')
def get_mult():
    try:
        a = float(input('first >>> '))
        b = float(input('second >>> '))
        print(f'the answer is: {mult(a,b)}')
        choose_operation()
    except:
        print('invalid syntax')
def get_diff():
    try:
        a = float(input('first >>> '))
        b = float(input('second >>> '))
        print(f'the answer is: {diff(a, b)}')
        choose_operation()
    except:
        print('invalid syntax')
def get_divi():
    try:
        a = float(input('first >>> '))
        b = float(input('second >>> '))
        print(f'the answer is: {divi(a, b)}')
        choose_operation()
    except:
        print('invalid syntax')

def suma(a,b):
    a = str(a)
    b = str(b)
    dot_a = a.find('.')
    dot_b = b.find('.')
    if dot_a == -1:
        a += '.0'
        dot_a = a.find('.')
    if dot_b == -1:
        b += '.0'
        dot_b = b.find('.')

    zeros = (max(len(a[dot_a + 1:]), len(b[dot_b + 1:]))) * '0'
    d = '1'+zeros
    return ((float(a)*int(d)) + (float(b)*int(d)))/ int(d)

def mult(a,b):
    a = str(a)
    b = str(b)
    dot_a = a.find('.')
    dot_b = b.find('.')
    if dot_a == -1:
        a += '.0'
        dot_a = a.find('.')
    if dot_b == -1:
        b += '.0'
        dot_b = b.find('.')

    zeros = (min(len(a[dot_a + 1:]), len(b[dot_b + 1:]))) * '0'
    d = '1' + zeros
    return ((float(a)*int(d)) * (float(b)*int(d)))/ int(d+'0')

def diff(a, b):
    a = str(a)
    b = str(b)
    dot_a = a.find('.')
    dot_b = b.find('.')
    if dot_a == -1:
        a += '.0'
        dot_a = a.find('.')
    if dot_b == -1:
        b += '.0'
        dot_b = b.find('.')

    zeros = (max(len(a[dot_a + 1:]), len(b[dot_b + 1:]))) * '0'
    d = '1' + zeros
    return ((float(a) * int(d)) - (float(b) * int(d))) / int(d)

def divi(a, b):
    try:
        return float(a)/float(b)
    except:
        return 'Error'

if __name__ == '__main__':
    choose_operation()
