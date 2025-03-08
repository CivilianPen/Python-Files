for A in range(1000):
    k=0
    for x in range(1000):
        for y in range(1000):
            if ((x<6) <= (x**2 <A)) and ((y**2<=A)<=(y<=6)):
                k+=1
    if k == 1000*1000:
        print(A)
