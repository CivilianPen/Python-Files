def sum(a,b):
    a = str(a)
    b = str(b)
    dot_a = a.find('.')
    dot_b = b.find('.')
    if len(a[dot_a:])<len(b[dot_b:]):
        count = len(b[dot_b:])-len(a[dot_a:])
        a+='0'*count
    else:
        count = len(a[dot_a:])-len(b[dot_b:])
        b+='0'*count
    dec =str(int(a[:dot_a])+int(b[:dot_b]))
    suma_float = str(int(a[dot_a+1:])+int(b[dot_b+1:]))
    if len(suma_float) < max(len(a[dot_a:]),len(b[dot_b:])):
        return(f'{dec}.{suma_float}')
    else:
        return(f'{int(dec)+int(suma_float[0])}.{suma_float[1:]}')
while True:
    try:
        a = float(input('enter first floats >>> '))
        b = float(input('enter second floats >>> '))
        print(f'the answer is: {sum(a,b)}')
    except:
        print('invalid syntax')