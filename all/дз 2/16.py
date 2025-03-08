f = [0]*100
f[1] = 1

for n in range(1,100):
    f[n] = f[n-1] + n
