f = open('17.txt')
s = [int(n) for n in f]
count = 0
mx_15 = 0
mx_suma = 0
for i in range(len(s)):
    if s[i]%100 == 15:
        mx_15 = max(mx_15,s[i])


for i in range(len(s)-2):
    a = [s[i],s[i+1],s[i+2]]
    if sum(a) >= mx_15:
        if (len(str(a[0])) == 4 and len(str(a[1])) != 4 and len(str(a[2])) != 4) or (len(str(a[1])) == 4 and len(str(a[2])) != 4 and len(str(a[0])) != 4) or (len(str(a[2])) == 4 and len(str(a[1])) != 4 and len(str(a[0])) != 4):
            count+=1
            mx_suma = max(mx_suma,sum(a))
        
