def system(n: int):
    new = ''
    while n>0:
        new+=str(n%3)
        n//=3
    return new[::-1]

for x in range(2031,0,-1):
    I = 3**100 - x
    I_3 = system(I)
    if I_3.count('0')== 1:
        print(x)
        break