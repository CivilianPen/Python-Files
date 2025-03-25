n = int(input())
a = list(map(int, input().split()))
b=[]
g = []
g2 = []
x=1
maxx = 0
m=0
h=n
z=0
for i in range(0,n+1):
    while i+x < n:
        if a[i] != 0:
            b.append(a[i+x]/a[i])
            g.append(i)
            g2.append(i+x)
        else:
            b = [0]
        x+=1
        if x == n-i:
            x=1
            i+=1
maxx = max(b)
if maxx > 1:
    ans = b.index(maxx)
    print(g[ans]+1,g2[ans]+1)
else:
    print(0,0)
