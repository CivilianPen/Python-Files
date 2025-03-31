import sys
def choose_operation():
    all = '+-*/'
    the_type = input('+-*/:')
    if the_type == '+':
        get_sum()
    elif the_type == '-':
        print('coming soon')
        choose_operation()
    elif the_type == '*':
        get_mult()
        choose_operation()
    elif the_type == '/':
        print('coming soon')
        choose_operation()
    else:
        if the_type != 'exit':
            choose_operation()
        else:
            sys.exit()

def suma(a,b):
    a = str(a)
    b = str(b)
    dot_a = a.find('.')
    dot_b = b.find('.')

    if len(a[dot_a:]) < len(b[dot_b:]):
        count = len(b[dot_b:]) - len(a[dot_a:])
        a += '0' * count
    else:
        count = len(a[dot_a:]) - len(b[dot_b:])
        b += '0' * count
    dec = str(int(a[:dot_a]) + int(b[:dot_b]))
    suma_float = str(int(a[dot_a + 1:]) + int(b[dot_b + 1:]))
    zeros_a = ''
    zeros_b = ''
    for i in range(1, len(a)):
        if a[i] in '123456789':
            break
        else:
            zeros_a += a[i]
    for i in range(1, len(b)):
        if b[i] in '123456789':
            break
        else:
            zeros_b += b[i]
    zeros = min(zeros_a[1:], zeros_b[1:])

    if (len(suma_float) < max(len(a[dot_a + 1:]), len(b[dot_b + 1:])) - len(zeros)) and zeros != '':
        return(f'{dec}.{zeros + suma_float}')
    elif zeros != '' and float(suma_float) >= 10:
        return(f'{int(dec)}.{zeros[:-1] + suma_float}')
    elif float(suma_float) >= int('1' + '0' * max(len(a) - 2, len(b) - 2)):
        return(f'{int(dec) + int(suma_float[0])}.{suma_float[1:]}')
    elif float(suma_float) <= int('1' + '0' * max(len(a) - 2, len(b) - 2)):
        return(f'{int(dec)}.{zeros + suma_float}')


def mult(a,b):
    a = str(a)
    b = str(b)
    dot_a = a.find('.')
    dot_b = b.find('.')

    dec = str(int(a[:dot_a])*int(b[:dot_b]))
    mult_float = str(int(a[dot_a+1:])*int(b[dot_b+1:]))
    zeros = len(str(int(a[dot_a+1:])))+len(str(int(b[dot_b+1:])))-len(mult_float)
    mult_float = zeros * '0' + mult_float
    x = int(a[:dot_a])
    y = int(b[:dot_b])
    x_f = float('0.'+(a[dot_a+1:]))
    y_f = float('0.'+(b[dot_b+1:]))
    x_all = [y_f for i in range(x)]
    y_all = [x_f for i in range(y)]
    suma1 = 0
    suma2 = 0
    for i in range(0,len(x_all)):
        suma1 = suma(suma1,x_all[i])
    for i in range(0,len(y_all)):
        suma2 = suma(suma2,y_all[i])
    formula = suma(suma(dec+'.0','0.'+mult_float),suma(suma1,suma2))

    return formula,suma2
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

if __name__ == '__main__':
    choose_operation()
