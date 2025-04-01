f = open('27880.txt')
S,N = map(int, f.readline().split())
a = [int(i) for i in f]
#S,N = 9537,1916
#a = [80,30,50,40]
#S,N = 100,4
a = sorted(a)

files = []
i = 0
while sum(files)+a[i]<=S:
    files.append(a[i])
    i+=1

needed = S-sum(files)

for i in range(needed,0,-1):
    if files[-1]+i in a and sum(files)+i<=S:
        files[-1] = a[a.index(files[-1]+i)]

print(len(files),files[-1])
