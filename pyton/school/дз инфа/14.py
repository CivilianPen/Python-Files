al = '0123456789abcd'

for x in al:
    for y in al:
    
        s = int('14'+y+'5'+x+'2',14)+int('31'+x+'2'+y+'3',14)
        if s%9==0:
            print(int(x,14),int(y,14),s//9)
