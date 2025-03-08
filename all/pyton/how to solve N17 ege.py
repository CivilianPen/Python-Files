f = open('17.txt')
s = f.readlines()
count = 0
mi = 100000
mx = -100000
for i in range(len(s)):
    s[i] = int(s[i])
    if s[i] < mi and abs(s[i])%10 == 6:
        mi = s[i]
        
for i in range(len(s)-1):
    if (abs(s[i])%10 == 6 and abs(s[i+1])%10!=6)or(abs(s[i+1])%10 == 6 and abs(s[i])%10!=6):
        if (s[i]**2 + s[i+1]**2) < mi**2:
            count+=1
            mx = max(mx,(s[i]**2 + s[i+1]**2))

print(count,mx)
