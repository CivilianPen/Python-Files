N = 998871
f = open('7.txt').readlines()
m = []
for i in f:
    m.append(list(map(int, i.split())))

m = sorted(m)
l = 0
mx = 0
for i in range(len(m)):
    if m[i][0] == m[i+1][0]:
        if m[i][1] == m[i+1][1]+1 or m[i][1] == m[i+1][1]:
            l+=1

