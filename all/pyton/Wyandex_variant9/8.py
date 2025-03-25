from itertools import product

arr = product('АВЕНС', repeat = 5)
count = 0
for i in arr:
    s = ''.join(i)
    if s[0] == 'Н' and s.count('В')==2:
        if len(s) == len(set(s))+1:
            count+=1
print(count)
