f = open('9.csv').readlines()
count = 0
arr = []
for i in f:
    x = list(map(int, i.split(';')))
    arr.append(x)
for i in range(len(arr)):
    mx = max(arr[i])
    suma_treh_drugih = sum(arr[i])-mx
    seted = set(arr[i])
    if mx < suma_treh_drugih:
        if len(arr[i])-1 == len(seted):
            count+=1

print(count)