n = 245756
a = [i for i in range(n+1)]
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n + 1, i):
            a[j] = 0
    i += 1

for i in lst:
    if i >= 245690:
        print(i,i-245689)

