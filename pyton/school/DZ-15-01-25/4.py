s = open('24_59849.txt').read()

no = 'QRSTUVWXYZ'

for i in no:
    s=s.replace(i,'-')

mx = 0
splt = s.split('-')
for i in splt:
    mx = max(len(i),mx)

print(mx)