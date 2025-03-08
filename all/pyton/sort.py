from random import randint
import timeit

n = 100
a = [0]*100
for i in range(n):
    a[i] = randint(-100,100)

start_time = timeit.default_timer()
for j in range(n):
    for i in range(n):
        if a[i] > a[j]:
            a[i], a[j] = a[j],a[i]
            
print(a[randint(10,20)])
if a == sorted(a):
    print(timeit.default_timer() - start_time)
else:
    print('daun')