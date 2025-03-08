f = [0]*100
f[4] = 1
for n in range(4,36):
    f[n] += f[n-1]
    if n%3 == 0:
        f[n] += f[n//3]
print(f[34])
