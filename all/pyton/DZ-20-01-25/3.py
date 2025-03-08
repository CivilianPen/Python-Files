s = open('3.txt').read()
mx = 1
count = 1
for i in range(len(s)-1):
    if s[i] == 'R' and s[i+1] == 'R':
        count+=1
    else:
        mx = max(count,mx)
        count = 1
print(mx)