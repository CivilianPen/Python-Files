f = [0]*50
f2 = [0]*50
f2[12] = 1
f[1] = 1
for n in range(0,13):
    f[n]+=f[n-1]
    f[n]+=f[n//2]
for n in range(12,31):
    f2[n]+=f2[n-1]
    f2[n]+=f2[n//2]
print(f2[30]*f[12])
'''def f(x,y):
    if x==y:
        return 1
    if x < y:
        return 0
    if x > y:
        return f(x-1,y)+f(x//2,y)
print(f(30,12)*f(12,1))'''
