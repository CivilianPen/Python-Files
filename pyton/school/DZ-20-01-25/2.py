s = open('2.txt').read()
s = s.replace('A','A ').replace('B','B ').split(' ')
maxi = 0
for i in range(len(s)-2):
    c = s[i] + s[i+1]+ s[i+2][:-1]
    if c.count('A') == 1 and c.count('B') == 1:
        maxi= max(maxi, len(c))
c = s[-3] + s[-2]+ s[-1]
if c.count('A') == 1 and c.count('B') == 1:
    maxi= max(maxi, len(c))
print(maxi)