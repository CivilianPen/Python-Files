for i in range(1000,2000):
    k = str(i)

    if ('1' in k) or ('3' in k) or ('6' in k) or ('7' in k) or ('9' in k):
        k = k.replace('3','4')
        k = k.replace('7', '8')

        p = 1
        for j in k:
            p*=int(j)
        if p==256:
            print(i)
            break
