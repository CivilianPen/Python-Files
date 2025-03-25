nk = list(map(int, input().split()))
cost = list(map(int, input().split()))
r = nk[1]
n = nk[0]
x=[]
y=[]
z=[]
for i in range(0,n-r-1):
    x.append(cost[i]+cost[i+r+1])
    y.append(i)
    z.append(i+r+1)
    i+=1
ans = x.index(max(x))
print(y[ans]+1,z[ans]+1,x,y,z)


#from random import randint
#r = nk[1]
#n = nk[0]
#cost = [0]*n
#for i in range(n):
#   cost[i] = randint(0,100)
#print(cost)
