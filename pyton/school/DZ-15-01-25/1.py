'''
a = [0] * 20
a[3] = 1
for i in range(4, 16):
    a[i] += a[i - 1]
    a[i] += a[i - 4]
print(a[15])
'''
'''
def f(x,y):
    if x==y:
        return 1
    if x>y:
        return 0
    if x<y:
        return f(x+1,y)+f(x+4,y)

print(f(3,15))
'''