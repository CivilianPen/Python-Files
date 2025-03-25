c = 0
i = 700000

while c < 5:
    d = set()
    M = 0
    for j in range(2,i//2+1):
        if i%j == 0:
            d.add(i//j)
            d.add(j)
    if len(d) >= 2:
        M = max(d)+min(d)

    if M%10==4:
        print(i,M)
        c+=1

    i+=1