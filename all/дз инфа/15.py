B = [-42,-10,-8,2,16]
C = [-10,-4,2,15,23]
A = [i for i in range(500)]

for i in range(500):
    for x in range(1000):
        if ((x == i) <= (x in B) or (x in C)) == 0:
            A.remove(i)
print(sum(A))
