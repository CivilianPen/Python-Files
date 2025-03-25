
a = [0]*20
a[3] = 1

for i in range(4,13):
    a[i] += a[i - 1]
    a[i] += a[i - 2]
    if a[i] % 2 == 0:
        a[i] += a[i // 2]

    if i == 10:
        for j in range(1, i):
            a[j] = 0
print(a)
'''
def f(x,y):
    if x==y:
        return 1
    if x>y:
        return 0
    if x<y:
        return f(x+1,y)+f(x+2,y)+f(x*2,y)

print(f(3,10)*f(10,12))
'''