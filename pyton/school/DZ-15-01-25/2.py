'''
a = [0] * 40
a[7] = 1
for i in range(8, 21):
    a[i] += a[i - 1]
    a[i] += a[i - 3]
    if a[i]%3==0:
        a[i]+=a[i//3]

    if i == 14:
        for j in range(1, i):
            a[j] = 0
    if i == 15:
        a[i] = 0

print(a[20])
'''
'''
def f(x,y):
    if x==y:
        return 1
    if x>y or x == 15:
        return 0
    if x<y:
        return f(x+1,y)+f(x+3,y)+f(x*3,y)

print(f(7,14)*f(14,20))
'''